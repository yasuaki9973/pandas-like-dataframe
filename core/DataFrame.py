from core.Series import Series

ERROR_NO_001 = 'カラム名は文字列で指定してください。'


class DataFrame:

    def __init__(self, data_list):

        self.__columns = []

        values = {}
        count = 0

        for data in data_list:

            if not isinstance(data, dict):
                data = vars(data)

            for new_column in list(set(data.keys()) - set(self.__columns)):
                values[new_column] = [None] * count
                self.__columns.append(new_column)

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

    def __setitem__(self, new_column, values):
        self.__columns.append(new_column)
        self.__values[new_column] = values

    def __repr__(self):
        return '{}'.format(self.__values)


if __name__ == "__main__":
    pass
