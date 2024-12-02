from mlModules import mlForDB, runXTimesAndReturnAverageAccuracyAndHighestAccuracy 
from sklearn import svm
from sklearn.model_selection import cross_val_score, cross_validate

from modules import DB

dbEmbeddings =DB('websites', "embeddings")
clf=svm.LinearSVC() #<- better results than the rbf kernel below
#clf=svm.SVC(kernel='rbf')

mlForDB(dbEmbeddings, clf, 'SVM', 1, 2, 'embeddings')

''' # to run multiple 
print('For how many iterations? :')
x = input()
runXTimesAndReturnAverageAccuracyAndHighestAccuracy(int(x), clf, 'SVM', 'embeddings')
'''

''' #cross validation
embeddings, classifications=getEmbeddingsAndClassificationsFromDb('SVM')
X=embeddings
y=classifications

cross=cross_validate(clf, X, y, cv=20)
print(cross)
'''
#scores = cross_val_score(clf, X, y, cv=10)
#print(scores)
#crossValidation(clf, 'SVM')