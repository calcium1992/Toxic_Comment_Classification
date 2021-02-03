import numpy as np
from sklearn.naive_bayes import MultinomialNB


class NaiveBayer(object):
    def __init__(self, classes):
        self.models = {}
        self.classes = classes
        for cls in self.classes:
            self.models[cls] = MultinomialNB()

    def fit(self, x_train, y_train):
        for idx, cls in enumerate(self.classes):
            y_train_one_label = y_train[:, idx]
            self.models[cls].fit(x_train, y_train_one_label)

    def predict(self, x_test):
        y_pred = np.zeros((x_test.shape[0], len(self.classes)))
        for idx, cls in enumerate(self.classes):
            y_pred[:, idx] = self.models[cls].predict(x_test)
        return y_pred

    def predict_prob(self, x_test):
        y_pred = np.zeros((x_test.shape[0], len(self.classes)))
        for idx, cls in enumerate(self.classes):
            y_pred[:, idx] = self.models[cls].predict_proba(x_test)
        return y_pred