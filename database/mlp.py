from mlModules import mlForDB, runXTimesAndReturnAverageAccuracyAndHighestAccuracy
from modules import DB
from sklearn.neural_network import MLPClassifier

dbEmbeddings =DB('websites', "embeddings")


#'''
#clf = MLPClassifier(hidden_layer_sizes=(512,256,128,64,32), max_iter=300,activation = 'relu',solver='adam',random_state=1) #1

#clf = MLPClassifier(hidden_layer_sizes=(512,256,128,64,32,16), max_iter=300,activation = 'relu',solver='adam',random_state=1, early_stopping=True) #1

#clf = MLPClassifier(hidden_layer_sizes=(512,256,128,64,32,16,8,4), max_iter=300,activation = 'relu',solver='adam',random_state=1, early_stopping=False) #1

clf = MLPClassifier(hidden_layer_sizes=(512,256,128,64,32,16,8), max_iter=300,activation = 'relu',solver='adam',random_state=1, early_stopping=True)

#clf = MLPClassifier(hidden_layer_sizes=(8,4), max_iter=300,activation = 'identity',solver='sgd',random_state=1, early_stopping=True)

#clf = MLPClassifier(hidden_layer_sizes=(256,64,16), max_iter=300,activation = 'identity',solver='sgd',random_state=1, early_stopping=True)

'''
print('For how many iterations? :')
x = input()
runXTimesAndReturnAverageAccuracyAndHighestAccuracy(int(x), clf, 'MLP')
'''

mlForDB(dbEmbeddings, clf, 'MLP', 1, 2, 'features')
#'''    