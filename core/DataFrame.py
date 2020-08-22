
ERROR_NO_001 = 'カラム名は文字列で指定してください。'


class DataFrame:

    def __init__(self, data_list):

        self.__columns = []

        values = {}
        count = 0

        for data in data_list:

            if not isinstance(data, dict):
                data = vars(data)

            diffs = list(set(data.keys()) - set(self.__columns))

            if len(diffs):

                for diff in diffs:
                    values[diff] = [None] * count
                    self.__columns.append(diff)

            for column in self.__columns:
                values[column].append(data.get(column))

            count += 1

        self.__values = {key: Series(value) for key, value in values.items()}

    def __getitem__(self, columns):

        def get_column_data(column):

            if not isinstance(column, str):
                raise Exception(ERROR_NO_001)

            return self.__values[column]

        if isinstance(columns, str):
            return get_column_data(columns)
        elif isinstance(columns, list):
            return {column: get_column_data(column) for column in columns}
        else:
            raise Exception(ERROR_NO_001)

    def __repr__(self):
        return '{}'.format(self.__values)


class Series:

    def __init__(self, values):
        self.__values = values

    def __repr__(self):
        return '{}'.format(self.__values)


if __name__ == "__main__":
    pass
