from abc import ABC, abstractmethod


class BaseEstimator(ABC):
    """
    Abstract base class for all estimators
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def fit(self, X, Y) -> None:
        """
        Fit model to training data
        """
        pass

    @abstractmethod
    def predict(self, X) -> None:
        """
        Predict output based on input X
        """
        pass
