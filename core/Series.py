

class Series:

    def __init__(self, values):
        self.__values = values

    def __add__(self, other):

        if not isinstance(other, Series):
            other = Series([other] * len(self.__values))

        return Series([value1 + value2 for value1, value2 in zip(self.__values, other.__values)])

    def __radd__(self, other):

        if not isinstance(other, Series):
            other = Series([other] * len(self.__values))

        return Series([value1 + value2 for value1, value2 in zip(other.__values, self.__values)])

    def __repr__(self):
        return '{}'.format(self.__values)


if __name__ == "__main__":
    pass
