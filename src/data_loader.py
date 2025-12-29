import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data():
    """
    Load Iris dataset and return features & target
    """
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    return X, y, feature_names, target_names


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into train and test sets
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )
    return X_train, X_test, y_train, y_test
