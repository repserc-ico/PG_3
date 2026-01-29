import ezsheets
#サンプルデータ "produceSales.xlsx" をchapter14にコピーしておいてください
ss = ezsheets.upload("produceSales.xlsx")
sheet = ss[0]
#print(sheet.getRow(1))  #1行目の内容をリストにセット
#print(sheet.getRow(2))  #2行目の内容をリストにセット
#print(sheet.getColumn(1))  #1列目の内容をリストにセット
#print(sheet.getColumn('B'))  #A列目の内容をリストにセット

print(sheet.getRow(3))  #3行目の内容を表示
sheet.updateRow(3, ["Pumpkin", "11.50", "20", "230"] )
print(sheet.getRow(3))  #書き換えた3行目を表示

column1 = sheet.getColumn(1)    #1列目の内容をリストにセット
for i, value in enumerate(column1):
    column1[i] = value.upper()  #英大文字に変換
sheet.updateColumn(1, column1)

print(sheet.rowCount)   #シートの行数
print(sheet.columnCount)    #シートの列数
#シートの列数、行数を変更する（オーバーした列/行はカットされる）
sheet.columnCount = 4
sheet.rowCount = 8