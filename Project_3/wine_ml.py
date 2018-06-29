from sklearn import datasets, svm, tree, naive_bayes
from sklearn.model_selection import train_test_split
import time

# Carrega base de dados
wine = datasets.load_wine()
features = wine.data
labels = wine.target

train_feats, test_feats, train_labels, test_labels = train_test_split(features, labels, test_size=0.2)

# SVM with linear kernel
algoritmo1 = svm.SVC(kernel='linear')

# Decision Tree Classifier
algoritmo2 = tree.DecisionTreeClassifier()

# Naive Bayes
algoritmo3 = naive_bayes.GaussianNB()

# Mostra os resultados
algorithms = [algoritmo1, algoritmo2, algoritmo3]
strategies = ['SVM with linear kernel', 'Decision Tree Classifier', 'Naive Bayes']
for index, alg in enumerate(algorithms):
    time_start = time.time()

    alg.fit(train_feats, train_labels)
    prediction = alg.predict(test_feats) # Realiza as predições

    time_end = time.time()
    time_total = time_end - time_start

    score = 0
    for i in range(len(prediction)):
        if prediction[i] == test_labels[i]:
            score += 1

    print('\n' + strategies[index])
    print('Predições:', prediction)
    print('Precisão: ' + str(round((score / len(prediction)) * 100, 3)) + '%')
    print('Tempo: ' + str(time_total) + 's')
