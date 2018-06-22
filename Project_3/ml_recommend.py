import numpy as np 
import pandas as pd 

header = ['movieId', 'title', 'genres']
df = pd.read_csv('ml-latest-small/movies.csv', sep='/t', names=header, engine='python')

n_movies = df.movieId.unique().shape[0]
print 'Number of movies = ' + str(n_movies)

