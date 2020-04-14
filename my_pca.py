# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall
# April 2020
# my_pca.py
# Utilize sci-kits pca method.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from sklearn.decomposition import PCA


class myPCA:
    def __init__(self, n_components=2):
        self.pca = PCA(n_components=n_components)

    def fit(self, X):
        return self.pca.fit_transform(X)

    def transform(self, X):
        return self.pca.transform(X)
