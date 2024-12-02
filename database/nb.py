# naive bayes 
from mlModules import mlForDB, runXTimesAndReturnAverageAccuracyAndHighestAccuracy
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from modules import DB

dbEmbeddings =DB('websites', "embeddings")
clf=GaussianNB() #got better results than the multinomialNB below
#clf=MultinomialNB() 
mlForDB(dbEmbeddings, clf, 'NB', 1, 2, 'features')
