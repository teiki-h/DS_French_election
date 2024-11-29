import pandas as pd
xl_file = pd.ExcelFile('input/effectifs_15_22.xlsx')

dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}

dfs1 = pd.read_excel('input/effectifs_15_22.xlsx', sheet_name=None)

for key, value in dfs1.items():
    print(key)