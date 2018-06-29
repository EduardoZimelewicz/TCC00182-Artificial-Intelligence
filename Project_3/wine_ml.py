from __future__ import division  # only for Python 2
from sklearn import datasets
from sklearn import svm
from sklearn import tree
from sklearn import naive_bayes
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts

wine = datasets.load_wine()

features = wine.data
labels = wine.target

train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size=0.2)

# SVM with linear kernel
algoritmo1 = svm.SVC(kernel='linear')

# Decision Tree Classifier
algoritmo2 = tree.DecisionTreeClassifier()

# Naive Bayes
algoritmo3 = naive_bayes.GaussianNB()

t_1 = time.time()
algoritmo1.fit(train_feats, train_labels)
t_2 = time.time()
t_algo_fit_1 = t_2 - t_1

t_1 = time.time()
algoritmo2.fit(train_feats, train_labels)
t_2 = time.time()
t_algo_fit_2 = t_2 - t_1

t_1 = time.time()
algoritmo3.fit(train_feats, train_labels)
t_2 = time.time()
t_algo_fit_3 = t_2 - t_1

t_1 = time.time()
predictions1 = algoritmo1.predict(test_feats)
t_2 = time.time()
print "\nPredictions:", predictions1
t_algo_1 = t_2 - t_1

t_1 = time.time()
predictions2 = algoritmo2.predict(test_feats)
t_2 = time.time()
print "\nPredictions:", predictions2
t_algo_2 = t_2 - t_1

t_1 = time.time()
predictions3 = algoritmo3.predict(test_feats)
t_2 = time.time()
print "\nPredictions:", predictions3
t_algo_3 = t_2 - t_1

print "\n"

score = 0
for i in range(len(predictions1)):
    if predictions1[i] == test_labels[i]:
        score += 1

accu1 = (score / len(predictions1))
print "SVM with linear kernel\n"
print "Fit_time:", t_algo_fit_1, "\n"
print "Time:", t_algo_1, "\n"
print "Accuracy:", accu1, "\n"

score = 0
for i in range(len(predictions2)):
    if predictions2[i] == test_labels[i]:
        score += 1

accu2 = (score / len(predictions1))
print "Decision Tree Classifier\n"
print "Fit_time:", t_algo_fit_2, "\n"
print "Time:", t_algo_2, "\n"
print "Accuracy:", accu2, "\n"

score = 0
for i in range(len(predictions3)):
    if predictions3[i] == test_labels[i]:
        score += 1

accu3 = (score / len(predictions1))
print "Naive Bayes\n"
print "Fit_time:", t_algo_fit_3, "\n"
print "Time:", t_algo_3, "\n"
print "Accuracy:", accu3, "\n"