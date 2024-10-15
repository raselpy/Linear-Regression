import numpy as np

class LinearRegression(object):
    def __init__(self, eta=0.1, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)
        self.w = np.ones(X.shape[1])
        m = X.shape[0]

        for _ in range(self.n_iter):
            output = X.dot(self.w)
            errors = y - output
            self.w += self.eta / m * errors.dot(X)
        return self

    def predict(self, X):
        return np.insert(X, 0, 1, axis=1).dot(self.w)


X = np.array([[0,1], [1,2], [2,3], [3,4]])
y = np.array([0, 1, 2, 3])

regr = LinearRegression().fit(X, y)
print(regr.w)
print(regr.predict([[5,6],[100,110]]))