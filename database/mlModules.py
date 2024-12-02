#Import scikit-learn dataset library
 #,datasets
from sklearn.model_selection import train_test_split
from modules import DB
from joblib import dump, load # <- to save the model in a file and load it from it
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay#, roc_auc_score
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from feature import generateFeatureInput


'''
db= DB("websites", "embeddings")

for x in db.find({'real_type': {'$exists': True}}):
    print(x['feature_information'])
'''

dbEmbeddings =DB('websites', "embeddings")
#dbTraining = DB('websites', "training")
#dbTesting = DB('websites', "testing")

def getValueOfType(string):
    match string:
        case 'IGV':
            return 2
        case 'IV':
            return 1
        case 'noIV':
            return 0
def getValueOfType_vector(string):
    '''
    match string:
        case 'IGV':
            return (1,0)
        case 'noIV':
            return (0,1)
        case _:
            print('!!!!!!!!!!!!wrong Classification !!!!!!!!!!!!!!!!')
    ''' #uncomment the part above for binary classification
    match string:
        case 'IGV':
            return (1,0,0)
        case 'IV':
            return (0,1,0)
        case 'noIV':
            return (0,0,1)
        case _:
            print('!!!!!!!!!!!!wrong Classification !!!!!!!!!!!!!!!!')
    #'''

def getEmbeddingsAndClassificationsFromDb(mlType, db=dbEmbeddings, classificationType='multiclass'):
    websites=''
    if classificationType=='multiclass':
        websites = db.find({'real_type': {'$exists': True}}) # for multiclass classification
    elif classificationType=='binary':
        websites=db.find({'real_type' : {'$in' : ["IGV", "noIV"]}}) # for binary classification
    else:
        print("wrong classification type")
    embeddings = []
    classifications=[]
    for website in websites:
        embeddings.append(website['embedding'])
        if mlType=='MLP':
            classifications.append(getValueOfType_vector(website['real_type']))
        else: 
            classifications.append(getValueOfType(website['real_type']))
    return np.array(embeddings), np.array(classifications)

def getFeatureInputs(mlType, db=dbEmbeddings):
    websites = db.find({'real_type': {'$exists': True}})
    featureInputs = []
    classifications=[]
    for website in websites:
        featureInputs.append(generateFeatureInput(website['feature_information']))
        if mlType=='MLP':
            classifications.append(getValueOfType_vector(website['real_type']))
        else: 
            classifications.append(getValueOfType(website['real_type']))
    return np.array(featureInputs), np.array(classifications)

def saveModel(model, filename):
    '''Saves a model as a pickle file.
    Takes a model and a filename as input.'''
    with open(f"{filename}.pkl", "wb") as f:
        dump(model, f, protocol=5)
def getModel(filename):
    '''Loads a model from a given file location.
    Takes a filename as input. Has to have an existing pickle file (.pkl)
    '''
    with open(f"{filename}.pkl", "rb") as f:
        model = load(f)
        return model

def printMetrics(clf, X_val, y_val, mlType):
    preds = clf.predict(X_val)
    print(clf.classes_)
    #print(preds)
    accuracy = accuracy_score(y_val, preds)
    print('accuracy: ',accuracy)
    if mlType=='MLP': #create plot for loss function in case the mlType is MLP
        from mlxtend.plotting import plot_confusion_matrix
        #from sklearn.model_selection import LearningCurveDisplay, learning_curve
        print('y_val: ',y_val)
        print('preds',preds)
        confusionMatrix=confusion_matrix(y_val.argmax(axis=1), preds.argmax(axis=1)) 
        #confusionMatrix=confusion_matrix(y_val, preds)
        print('Confusion Matrix: ')
        print(confusionMatrix)
        '''
        tcm =[]
        tcm.append([confusionMatrix[2][2], confusionMatrix[2][1], confusionMatrix[2][0]])
        tcm.append([confusionMatrix[1][2], confusionMatrix[1][1], confusionMatrix[1][0]])
        tcm.append([confusionMatrix[0][2], confusionMatrix[0][1], confusionMatrix[0][0]])
        '''
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(clf.loss_curve_)
        ax.set_xlabel('Number of iterations')
        ax.set_ylabel('Loss')
        #plt.savefig('C:\Users\philh\OneDrive\Pictures\ma_metrics\test.png')
        plt.show()
        #binary1 = np.array(tcm)
        binary1 = np.array(confusionMatrix)
        print('b:',binary1)
        fig, ax = plot_confusion_matrix(conf_mat=binary1, show_absolute=False,show_normed=True,colorbar=True, class_names=['noIV', 'IV', 'IGV']) 
        #fig, ax = plot_confusion_matrix(conf_mat=binary1, show_absolute=False,show_normed=True,colorbar=True, class_names=['noIV', 'IGV']) # uncomment for binary classification
        plt.show()

    else:
        from mlxtend.plotting import plot_confusion_matrix
        confusionMatrix=confusion_matrix(y_val, preds) 
        print('Confusion Matrix: ')
        print(confusionMatrix)
        binary1 = np.array(confusionMatrix)
        fig, ax = plot_confusion_matrix(conf_mat=binary1, show_absolute=True,show_normed=True,colorbar=True, class_names=['noIV', 'IV', 'IGV'])
        #fig, ax = plot_confusion_matrix(conf_mat=binary1, show_absolute=False,show_normed=True,colorbar=True, class_names=['noIV', 'IV', 'IGV'])
        #fig, ax = plot_confusion_matrix(conf_mat=binary1, show_absolute=False,show_normed=True,colorbar=True, class_names=['noIV', 'IGV']) # uncomment for binary classification
        plt.show()
    precision = precision_score(y_val, preds, average='macro')
    recall = recall_score(y_val, preds, average='macro')
    f1 = f1_score(y_val, preds, average='macro')
    print('precision: ', precision)
    print('recall: ', recall)
    print('f1: ', f1)

def mlForDB(db, clf, mlType, seed1, seed2, inputDataFormat='embeddings', classificationType='multiclass'):
    '''
    returns the accuracy for a ML classifier with a 70-15-15 training/test/validation split
    '''
    X=0
    y=0
    if inputDataFormat=='embeddings':
        X, y = getEmbeddingsAndClassificationsFromDb(mlType, db, classificationType=classificationType)
    elif inputDataFormat=='features':
        X,y = getFeatureInputs(mlType, db)
    else:
         'Wrong Input'

    # split data in training, test and validation (70, 15, 15)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=seed1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15/0.85, random_state=seed2) # 0.85*(0.15/0.85) = 0.15
    clf.fit(X_train, y_train)
    saveModel(clf, f'{mlType}_test')

    # print metrics
    printMetrics(clf, X_val, y_val, mlType)
    preds = clf.predict(X_val)
    accuracy = accuracy_score(y_val, preds)

    return accuracy
'''
def crossValidation(clf, mlType):
    from sklearn.model_selection import cross_val_score
    #
    returns the scores for cross-validation
    
    embeddings, classifications=getEmbeddingsAndClassificationsFromDb(mlType, dbEmbeddings)
    #print(embeddings.shape)
    #print(classifications.shape)
    #print(embeddings.shape[0]==classifications.shape[0])

    X=embeddings
    y=classifications

    # split data in training, test and validation (70, 15, 15)
    
    scores = cross_val_score(clf, X, y, cv=10)
    print(scores)
    #return scores
   ''' 
def getFullMlTypeName(string):
    match string:
        case 'RF':
            return 'Random Forrest'
        case 'SVM':
            return 'Support Vector Machine'
        case 'NB':
            return 'Naive Bayes'
        case 'MLP':
            return 'Multi Layer Perceptron'
        
def runXTimesAndReturnAverageAccuracyAndHighestAccuracy(x, clf, mlType, inputDataFormat):
    '''
    Enables the calculation for multiple seeds, to caompare the results for different dataset seeds'''
    highestAccuracy=0
    totalAccuracy=0
    seed=0
    for i in tqdm(range(0, x)):
        currentAccuracy=mlForDB(dbEmbeddings, clf, mlType, i, i+1, inputDataFormat)
        if currentAccuracy>highestAccuracy:
            highestAccuracy=currentAccuracy
            seed=i
        totalAccuracy+=currentAccuracy
    print('<---- For', x, ' runs of ', mlType, '------->')
    print('The highest Accuracy was ', highestAccuracy, ' with the seeds ', seed, ' and ', seed+1)
    print('The Average Accuracy was ', totalAccuracy/x)