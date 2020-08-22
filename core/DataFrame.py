
ERROR_NO_001 = 'カラム名は文字列で指定してください。'


class DataFrame:

    def __init__(self, data_list):

        self.__values = {}
        self.__columns = []
        self.__len = 0

        for data in data_list:

            if not isinstance(data, dict):
                data = vars(data)

            diffs = list(set(data.keys()) - set(self.__columns))

            if len(diffs):

                for diff in diffs:
                    self.__values[diff] = Series(self.__len)
                    self.__columns.append(diff)

            for column in self.__columns:
                self.__values[column].append(data.get(column))

            self.__len += 1

    def __getitem__(self, columns):

        if isinstance(columns, str):
            return self.__get_column_data(columns)
        elif isinstance(columns, list):
            return {column: self.__get_column_data(column) for column in columns}
        else:
            raise Exception(ERROR_NO_001)

    def __repr__(self):
        return '{}'.format(self.__values)

    def __get_column_data(self, column):

        if not isinstance(column, str):
            raise Exception(ERROR_NO_001)

        return self.__values[column]


class Series:

    def __init__(self, count):
        self.__values = [None] * count

    def append(self, data):
        self.__values.append(data)

    def __repr__(self):
        return '{}'.format(self.__values)


if __name__ == "__main__":
    pass
