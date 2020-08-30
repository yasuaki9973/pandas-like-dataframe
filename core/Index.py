from util.message import ERROR_MESSAGE_NO_001


class Index:

    def __init__(self, values):

        if isinstance(values, int):
            count = values
            self.__values = {i: i for i in range(count)}

        elif isinstance(values, list):
            self.__values = {value: index for index, value in enumerate(values)}

        else:
            raise Exception(ERROR_MESSAGE_NO_001)

    def convert_index(self, index):
        return self.__values.get(index)

    def get_indexes(self):
        return self.__values.items()

    def __repr__(self):
        return '{}'.format(self.__values)


if __name__ == "__main__":
    pass
