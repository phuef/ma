# code adapted from https://simulationbased.com/2021/01/05/introduction-to-t-sne-in-python-with-scikit-learn/ # unfortunally I couldn't get this to run due to some error with parallelization
from threadpoolctl import threadpool_info, threadpool_limits
info = threadpool_info()
print(info)
from mlModules import getEmbeddingsAndClassificationsFromDb
from sklearn.manifold import TSNE
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


with threadpool_limits(limits=1):
    from sklearn.manifold import TSNE
    #tsne = TSNE()

    X, y=getEmbeddingsAndClassificationsFromDb('SVM')
    print(X.shape)
    print(y.shape)
    np.unique(y)
    n_components = 2
    tsne = TSNE(n_components)
    tsne_result = tsne.fit_transform(X)
    tsne_result.shape

    # Plot the result of our TSNE with the label color coded
    # A lot of the stuff here is about making the plot look pretty and not TSNE
    tsne_result_df = pd.DataFrame({'tsne_1': tsne_result[:,0], 'tsne_2': tsne_result[:,1], 'label': y})
    fig, ax = plt.subplots(1)
    sns.scatterplot(x='tsne_1', y='tsne_2', hue='label', data=tsne_result_df, ax=ax,s=120)
    lim = (tsne_result.min()-5, tsne_result.max()+5)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect('equal')
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)