import xlrd

from FALLOW import constants, excel_utils

DATA_FILE = '../../Book1.xls'
SHEET = 'Sheet1'

wb = xlrd.open_workbook(DATA_FILE)
ws = wb.sheet_by_name(SHEET)

landuse = excel_utils.read_table(
    constants.LAND_USE,
    constants.LAND_PROPERTY,
    excel_utils.get_table(ws, start_col=3, start_row=5, end_col=5, end_row=20)
)

biophysics1 = excel_utils.read_table(
    constants.LAND_COVER,
    constants.LANDAGE_PROPERTY,
    excel_utils.get_table(ws, 1, 27, 16, 77)
)

biophysics2 = excel_utils.read_table(
    constants.LAND_USE,
    constants.BIOPHYSIC_PROPERTY,
    excel_utils.get_table(ws, 1, 83, 14, 98)
)

economic = excel_utils.read_table(
    constants.LAND_USE,
    constants.ECONOMIC_PROPERTY,
    excel_utils.get_table(ws, 1, 105, 17, 120)
)

labour = excel_utils.read_table(
    constants.PRODUCT,
    constants.LABOUR_PROPERTY,
    excel_utils.get_table(ws, 3, 124, 5, 175)
)

social_cultural = excel_utils.read_table(
    constants.LAND_USE,
    constants.SOCIAL_CULTURAL_PROPERTY,
    excel_utils.get_table(ws, 4, 180, 7, 195)
)

demography = excel_utils.read_column(
    constants.DEMOGRAPHY_PROPERTY,
    ws.col_values(4, 200, 206)
)

farmer = excel_utils.read_table(
    constants.FARMER_PROPERTY,
    constants.FARMER_SYSTEM,
    excel_utils.get_table(ws, 4, 210, 6, 214)
)

environment = excel_utils.read_column(
    constants.ENVIRONMENT_PROPERTY,
    ws.col_values(3, 216, 224)
)
