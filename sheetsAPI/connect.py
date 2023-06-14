import gspread
import pandas as pd

SHEET_ID = '1NOrEanJxSDMLd3__fg-kho4mSJYP2VL8Zs-ziS_8iIc'
SHEET_NAME = 'Sheet1'

gc = gspread.service_account('credentials.json')
spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet(SHEET_NAME)
rows = worksheet.get_all_records()

print(rows[:5])
print('==============================')

df = pd.DataFrame(rows)
print(df.head())