from mlModules import mlForDB, runXTimesAndReturnAverageAccuracyAndHighestAccuracy
from sklearn.ensemble import RandomForestClassifier
from modules import DB

dbEmbeddings =DB('websites', "embeddings")

clf=RandomForestClassifier()
mlForDB(dbEmbeddings, clf, 'RF', 1, 2, 'features')

'''
print('For how many iterations? :')
x = input()runXTimesAndReturnAverageAccuracyAndHighestAccuracy(int(x), clf, 'RF', 'embeddings') # <-- does multiple runs for different seeds
'''