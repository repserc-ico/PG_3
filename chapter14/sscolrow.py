import ezsheets

ss = ezsheets.upload("produceSales.xlsx")
sheet = ss[0]
print(sheet.getRow(1))  #1行目の内容をリストにセット
print(sheet.getRow(2))  #2行目の内容をリストにセット
print(sheet.getColumn(1))  #1列目の内容をリストにセット
print(sheet.getColumn('A'))  #A列目の内容をリストにセット
