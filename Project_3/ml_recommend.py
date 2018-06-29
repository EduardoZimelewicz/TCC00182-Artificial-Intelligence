import numpy
import pandas as csv_manager
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import scipy.sparse
from scipy.sparse.linalg import svds
from sklearn import model_selection

"""
    TÉCNICAS
    
1. Usuário-Item
    - Recomenda filmes que usuários com gostos semelhantes gostaram(avaliações parecidas)


2. Item-Item
    - Recomenda filmes semelhantes ao filme escolhido(procura usuários que gostaram dele e de outros filmes em comum)


OBS: Estamos fazendo a técnica #2

"""

# ---------------------------------------------------------- CARREGAMENTO DE BASE DE DADOS E INICIALIZAÇÃO DE VARIÁVEIS
# Carrega os dados dos arquivos .csv
movies = csv_manager.read_csv('ml-latest-small/movies.csv', sep=',', header=None, names=['id', 'title', 'genres'])
ratings = csv_manager.read_csv('ml-latest-small/ratings.csv', sep=',', header=None, names=['user_id', 'movie_id', 'rating', 'timestamp'])

# Quantidades
n_movies = movies.id.unique().shape[0]  # Filmes
n_genres = movies.genres.unique().shape[0]  # Gêneros
n_users = ratings.user_id.unique().shape[0]  # Usuários
n_ratings = ratings.movie_id.unique().shape[0]  # Avaliações

print("Filmes: \t" + str(n_movies) + "\t | \t Gêneros diferentes: \t" + str(n_genres))
print("Usuários: \t" + str(n_users) + "\t\t | \t Filmes avaliados: \t\t" + str(n_ratings))

# ----------------------------------------------------------------------------------------------- TREINO SUPERVISIONADO
# 75% Treino, 25% Teste
train_data, test_data = model_selection.train_test_split(ratings, test_size=0.25)  # test_size=25%

# Associa os ids dos filmes com indices da matriz de treino e de teste
# exemplo: { id_filme: 2055, index_matriz: 1616 }
# id_filme varia NÃO sequencialmente de 1 até 164979
# index_matriz varia sequencialmente de 0 até 9125
movies_id_index = {}
for index, movie in enumerate(movies.id.values):
    movies_id_index[str(movie)] = index

# ------------------------------------------------------------------------------------------------------------ MATRIZES
# Matriz Usuário-Item de TREINO
train_data_matrix = numpy.zeros((n_users, n_movies))
for line in train_data.itertuples():
    train_data_matrix[line.user_id - 1, movies_id_index[str(line.movie_id)]] = line.rating

# Matriz Usuário-Item de TESTE
test_data_matrix = numpy.zeros((n_users, n_movies))
for line in test_data.itertuples():
    test_data_matrix[line.user_id - 1, movies_id_index[str(line.movie_id)]] = line.rating

users_similarity = pairwise_distances(train_data_matrix, metric='cosine')
ratings_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')


# ------------------------------------------------------------------------------------------------------------ PREDIÇÃO
def predict(ratings, similarity, type='user'):
    somatorio = numpy.abs(similarity).sum(axis=1)  # [[1.0, -3.0, 4.0]] => [[1.0, 3.0, 4.0]] => [8.0]
    return ratings.dot(similarity) / numpy.array([somatorio])


item_prediction = predict(train_data_matrix, ratings_similarity, type='item')
print(item_prediction)


# Normaliza os votos
# RMSE - Root Mean Squared Error
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()

    return sqrt(mean_squared_error(prediction, ground_truth))


u, s, vt = svds(train_data_matrix, k=5)
s_diag_matrix= numpy.diag(s)
X_pred = numpy.dot(numpy.dot(u, s_diag_matrix), vt)
print('User-based CF MSE: ' + str(rmse(X_pred, test_data_matrix)))

# print('User-based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix)))
# print('Item-based CF RMSE: ' + str(rmse(item_prediction, test_data_matrix)))

sparsity = round(1.0 - len(ratings) / float(n_users * n_ratings), 3)
print('\nA base da dados possui esparsidade de ' + str(sparsity * 100) + '%')

# ------------------------------------------------------------------------------------------------------------ ANTIGO
# tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0, stop_words='english')
# tfidf_matrix = tf.fit_transform(movies.genres)
# print(tfidf_matrix)
# #cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
# #cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
# cosine_similarities = pairwise_kernels(tfidf_matrix, tfidf_matrix)
#
# results = {}
#
# for idx, row in movies.iterrows():
#     # linear-kernel
#     similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
#     similar_items = [(cosine_similarities[idx][i], movies[0][i]) for i in similar_indices]
#
#     # First item is the item itself, so remove it.
#     # Each dictionary entry is like: [(1,2), (3,4)], with each tuple being (score, item_id)
#     results[row[0]] = similar_items[1:]
#
# print('done!')
#
# # hacky little function to get a friendly item name from the description field, given an item ID
# def item(id):
#     return movies.loc[movies[0] == id][1].tolist()[0]
#
# # Just reads the results out of the dictionary. No real logic here.
# def recommend(item_id, num):
#     print("Recommending " + str(num) + " movies similar to " + item(item_id) + "...")
#     print("-------")
#     recs = results[item_id][:num]
#     for rec in recs:
#         print("Recommended: " + item(rec[1]) + "\t\t (score:" + str(rec[0]) + ")")
#
# # Just plug in any item id here (1-500), and the number of recommendations you want (1-99)
# # You can get a list of valid item IDs by evaluating the variable 'ds', or a few are listed below
#
# recommend(item_id=95473, num=10)
