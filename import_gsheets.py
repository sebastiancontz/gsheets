import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

JSON_CRED = 'plotly-281608-76ee7620228f.json'


def credentials(json_file):
    '''

    Funcion que genera credenciales para logearse al servicio de google.

    Args:
        json_file (str): nombre de archivo json que contiene la key de API
    Returns:
        google_cred: variable que contiene la credencial validada por el servicio gspread.authorize()

    '''
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            json_file, scope)
    google_cred = gspread.authorize(credentials)
    return google_cred


def import_gsheet(workbook, sheet: int =0):
    '''

    Funcion que devuelve un dataframe de pandas a partir del nombre del libro de google sheets,
    por defecto retorna la primera hoja.

    Args:
        workbook (str): nombre del workbook de google sheets.
        sheet (int): número de la hoja del workbook, comienza en 0.
    Returns:
        dataframe: dataframe de pandas con la data descargada de google sheets.
        
    '''
    gc = credentials(JSON_CRED)
    wks = gc.open(workbook).get_workbook(sheet)
    data = wks.get_all_values()
    headers = data.pop(0)
    dataframe = pd.DataFrame(data, columns=headers)
    return dataframe


def get_gsheets(worksheet):
    '''

    Funcion que lista todas las hojas encontradas dentro de un workbook de google sheets

    Args:
        workbook (str): nombre del workbook de google sheets.    
    '''
    gc = credentials(JSON_CRED)
    wks = gc.open(worksheet)
    print("Hojas encontradas:")
    for sheet in wks.worksheets():
        print(sheet)
