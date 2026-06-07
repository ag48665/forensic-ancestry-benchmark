import pandas as pd

url = (
    "https://www.fsigenetics.com/cms/10.1016/j.fsigen.2018.03.010/"
    "attachment/5ea7957a-80f6-4e8a-b3d4-6c6969653d3b/mmc3.xlsx"
)

print("Downloading AIM supplement...")
print(url)

xls = pd.ExcelFile(url)

print("Sheets:")
print(xls.sheet_names)

for sheet in xls.sheet_names:
    print("\n--- SHEET:", sheet, "---")
    df = pd.read_excel(url, sheet_name=sheet)
    print(df.head())
    print("Columns:", list(df.columns))
    print("Rows:", len(df))