
def get_table(sheet, start_col, start_row, end_col, end_row):
    return [sheet.col_values(_, start_row, end_row)
            for _ in range(start_col, end_col)]


def read_column(keys, values):
    """read column from excel file
    :param keys:
    :param values:
    :return: A adictionary with key, value merge from system, property
    """
    value = dict()
    valueIndex = 0
    for key in keys:
        if type(key) is dict:
            subKey = key.keys()[0]
            value[subKey] = {}
            valueIndex += 1
            for childrenKey in key[subKey]:
                value[subKey][childrenKey] = values[valueIndex]
                valueIndex += 1
        else:
            value[key] = values[valueIndex]
            valueIndex += 1

    return value


def read_table(keys, properties, values):
    """read table data
    :param keys:
    :param properties:
    :param values:
    :return: dictionary
    """
    value = dict()
    valueIndex = 0
    for property in properties:
        if type(property) is dict:
            subProperty = property.keys()[0]
            value[subProperty] = dict()
            for childProperty in property[subProperty]:
                if type(childProperty) is dict:
                    grandChildrenProperty = childProperty.keys()[0]
                    value[subProperty][grandChildrenProperty] = dict()
                    for grandChildProperty in \
                            childProperty[grandChildrenProperty]:
                        value[subProperty][grandChildrenProperty][
                            grandChildProperty
                        ] = read_column(keys, values[valueIndex])
                        valueIndex += 1
                else:
                    value[subProperty][
                        childProperty
                    ] = read_column(keys, values[valueIndex])
                    valueIndex += 1
        else:
            value[property] = read_column(keys, values[valueIndex])
            valueIndex += 1

    return value


if __name__ == '__main__':
    import xlrd
    from FALLOW import constants

    DATA_FILE = 'Book1.xls'
    SHEET = 'Sheet1'
    wb = xlrd.open_workbook(DATA_FILE)
    ws = wb.sheet_by_name(SHEET)
    values = ws.col_values(1, 27, 77)
    testData = read_column(constants.LAND_COVER, values)
    print testData

    values = [ws.col_values(col, 83, 98) for col in range(1, 14)]
    testTable = read_table(
        constants.LAND_USE,
        constants.BIOPHYSIC_PROPERTY,
        values
    )
    print testTable['storage properties']['probability to sell (0-1)']
