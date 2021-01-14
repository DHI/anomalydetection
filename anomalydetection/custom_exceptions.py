class WrongInputDataType(Exception):
    def __init__(self, message="Input data must be a pandas.Series."):
        self.message = message
        super().__init__(self.message)


class NotFittedError(Exception):
    def __init__(self, message="Please call fit() before detect().", tip=""):
        self.message = " ".join([message, tip])
        super().__init__(self.message)


class NoRangeDefinedError(NotFittedError):
    def __init__(self, message="Or specify min/max range when instantiating detector object."):
        super().__init__(message)