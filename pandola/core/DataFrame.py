from pandola.core.Series import Series
from pandola.core.Index import Index
from pandola.core.Location import Location
from pandola.util.message import ERROR_MESSAGE_NO_001


class DataFrame:

    def __init__(self, data_list):

        self.__columns = []

        if isinstance(data_list, list):
            self.__init_from_list(data_list)
        elif isinstance(data_list, dict):
            self.__init_from_dict(data_list)
        else:
            raise Exception(ERROR_MESSAGE_NO_001)

        def to_data_frame(values):
            return DataFrame(values)

        def to_series(values):
            return Series(values)

        self.loc = Location(self.__values, self.__columns, self.__index, to_data_frame, to_series)

    def to_dict(self, orient='records'):
        indexes = [value for _, value in self.__index.get_indexes()]
        return [self.loc[index].to_dict() for index in indexes]

    def __init_from_list(self, data_list):

        values = {}
        count = 0

        for data in data_list:

            if not isinstance(data, dict):
                data = vars(data)

            new_columns = list(set(data.keys()) - set(self.__columns))

            for column in list(data.keys()):

                if column in new_columns:
                    values[column] = [None] * count
                    self.__columns.append(column)

            for column in self.__columns:
                values[column].append(data.get(column))

            count += 1

        self.__values = values
        self.__index = Index(count)

    def __init_from_dict(self, data_list):
        self.__values = data_list
        self.__columns = list(data_list.keys())
        count = len(data_list[self.__columns[0]])
        self.__index = Index(count)

    def __get_column_data(self, column):

        if not isinstance(column, str):
            raise Exception(ERROR_MESSAGE_NO_001)

        return self.__values[column]

    def __getitem__(self, columns):

        if isinstance(columns, str):
            return Series(self.__get_column_data(columns))
        elif isinstance(columns, list):
            return DataFrame({column: self.__get_column_data(column) for column in columns})
        else:
            raise Exception(ERROR_MESSAGE_NO_001)

    def __setitem__(self, new_column, values):
        self.__columns.append(new_column)
        self.__values[new_column] = values

    def __repr__(self):
        return '{}, index:{}'.format(self.__values, self.__index)


if __name__ == "__main__":
    pass
