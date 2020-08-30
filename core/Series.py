from core.Index import Index
from util.message import ERROR_MESSAGE_NO_001


class Series:

    def __init__(self, values):

        if isinstance(values, list):
            self.__init_from_list(values)
        elif isinstance(values, dict):
            self.__init_from_dict(values)
        else:
            raise Exception(ERROR_MESSAGE_NO_001)

    def to_dict(self):
        return {key: self.__values[index] for key, index in self.__index.get_indexes()}

    def __init_from_list(self, values):
        self.__values = values
        self.__index = Index(len(values))

    def __init_from_dict(self, values):
        self.__values = list(values.values())
        self.__index = Index(list(values.keys()))

    def __add__(self, other):

        if not isinstance(other, Series):
            other = Series([other] * len(self.__values))

        return Series([value1 + value2 for value1, value2 in zip(self.__values, other.__values)])

    def __radd__(self, other):

        if not isinstance(other, Series):
            other = Series([other] * len(self.__values))

        return Series([value1 + value2 for value1, value2 in zip(other.__values, self.__values)])

    def __repr__(self):
        return '{}, index:{}'.format(self.__values, self.__index)


if __name__ == "__main__":
    pass
