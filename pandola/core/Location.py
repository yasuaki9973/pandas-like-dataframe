from pandola.util.message import ERROR_MESSAGE_NO_001


class Location:

    def __init__(self, values, columns, index, to_data_frame, to_series):
        self.__values = values
        self.__columns = columns
        self.__index = index
        self.__to_data_frame = to_data_frame
        self.__to_series = to_series

    def __get_row_data(self, row):

        if not isinstance(row, int):
            raise Exception(ERROR_MESSAGE_NO_001)

        row_data = {}

        for column in self.__columns:
            row_data[column] = self.__values.get(column)[self.__index.convert_index(row)]

        return row_data

    def __getitem__(self, rows):

        if isinstance(rows, int):
            return self.__to_series(self.__get_row_data(rows))
        elif isinstance(rows, list):
            return self.__to_data_frame([self.__get_row_data(row) for row in rows])
        else:
            raise Exception(ERROR_MESSAGE_NO_001)


if __name__ == "__main__":
    pass
