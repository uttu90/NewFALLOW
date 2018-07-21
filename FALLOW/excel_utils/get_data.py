import xlrd

from FALLOW import constants, excel_utils


def get_data_from_file(file_name, sheet_name):
    wb = xlrd.open_workbook(file_name)
    ws = wb.sheet_by_name(sheet_name)
    # for sheet in wb.sheets():
    #     print sheet.name

    # land_use_sheet = wb.sheet_by_name('Landuse')
    landuse = excel_utils.read_table(
        constants.LAND_USE,
        constants.LAND_PROPERTY,
        excel_utils.get_table(
            ws,
            start_col=3,
            start_row=4,
            end_col=5,
            end_row=19)
    )


    # biophysics1_sheet = wb.sheet_by_name('Biophysical1')
    biophysics1 = excel_utils.read_table(
        constants.LAND_COVER,
        constants.LANDAGE_PROPERTY,
        excel_utils.get_table(ws, 1, 24, 16, 74)
    )

    # biophysics2_sheet = wb.sheet_by_name('Biophysical2')
    biophysics2 = excel_utils.read_table(
        constants.LAND_USE,
        constants.BIOPHYSIC_PROPERTY,
        excel_utils.get_table(ws, 1, 78, 13, 93)
    )

    # economic_sheet = wb.sheet_by_name('Economic')
    economic = excel_utils.read_table(
        constants.LAND_USE,
        constants.ECONOMIC_PROPERTY,
        excel_utils.get_table(ws, 1, 98, 17, 113)
    )

    # demography_sheet = wb.sheet_by_name('Demography')
    demography = excel_utils.read_column(
        constants.DEMOGRAPHY_PROPERTY,
        ws.col_values(2, 190, 196)
    )
    farmer = excel_utils.read_table(
        constants.FARMER_PROPERTY,
        constants.FARMER_SYSTEM,
        excel_utils.get_table(ws, 2, 199, 4, 203)
    )

    # labour_sheet = wb.sheet_by_name('Labour')
    labour = excel_utils.read_table(
        constants.PRODUCT,
        constants.LABOUR_PROPERTY,
        excel_utils.get_table(ws, 1, 117, 3, 168)
    )

    # social_cultural_sheet = wb.sheet_by_name('Social')
    social_cultural = excel_utils.read_table(
        constants.LAND_USE,
        constants.SOCIAL_CULTURAL_PROPERTY,
        excel_utils.get_table(ws, 1, 172, 4, 187)
    )

    # environment_sheet = wb.sheet_by_name('Environment')
    environment = excel_utils.read_column(
        constants.ENVIRONMENT_PROPERTY,
        ws.col_values(1, 206, 214)
    )

    product_prices_time_series = excel_utils.read_time_series(
        constants.LAND_USE,
        excel_utils.get_table_by_row(ws, 1, 218, 101, 233)
    )

    extension_availability_time_series = excel_utils.read_time_series(
        constants.LAND_USE,
        excel_utils.get_table_by_row(ws, 1, 237, 101, 252)
    )

    subsidy_availability_time_series = excel_utils.read_time_series(
        constants.LAND_USE,
        excel_utils.get_table_by_row(ws, 1, 256, 101, 271)
    )

    return {
        'landuse': landuse,
        'biophysics1': biophysics1,
        'biophysics2': biophysics2,
        'economic': economic,
        'demography': demography,
        'farmer': farmer,
        'environment': environment,
        'labour': labour,
        'social_cultural': social_cultural,
        'product_price': product_prices_time_series,
        'extension_availability': extension_availability_time_series,
        'subsidy_avaibility': subsidy_availability_time_series
    }