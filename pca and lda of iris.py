from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
def load_data():
 return load_iris()
def load_data_tag():
 iris = load_data()
 return iris.data, iris.target
def PCA(data, n):
 from sklearn.decomposition import PCA
 pca = PCA(n_components=n)
 pca_result = pca.fit_transform(data.data)
 return pca_result
def LDA(data, n):
 from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
 lda = LDA(n_components=n)
 lda_result = lda.fit_transform(data.data, data.target)
 return lda_result
def plot(data, n):
 pca_result = PCA(data, n)
 lda_result = LDA(data, n)
 colors1 = '#00CED1'
 colors2 = '#DC143C'
 colors3 = '#000000'
 plt.subplot(1, 2, 1)
 plt.scatter(pca_result[data.target == 0, 0], pca_result[data.target == 0, 1], alpha=0.6, color=colors1)
 plt.scatter(pca_result[data.target == 1, 0], pca_result[data.target == 1, 1], alpha=0.6,color=colors2)
 plt.scatter(pca_result[data.target == 2, 0], pca_result[data.target == 2, 1], alpha=0.6, color=colors3)
 plt.title('PCA on iris')
 plt.subplot(1, 2, 2)
 plt.scatter(lda_result[data.target == 0, 0], lda_result[data.target == 0, 1], alpha=0.6, color=colors1)
 plt.scatter(lda_result[data.target == 1, 0], lda_result[data.target == 1, 1], alpha=0.6, color=colors2)
 plt.scatter(lda_result[data.target == 2, 0], lda_result[data.target == 2, 1], alpha=0.6, color=colors3)
 plt.title('LDA on iris')
 plt.show()

load_data()
load_data_tag()
plot(load_data(),3)