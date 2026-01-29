import ezsheets

ss = ezsheets.createSpreadsheet("Multiple Sheets")
print(ss.sheetTitles)   #最初は「シート1」しかない

ss.createSheet("Spam")
ss.createSheet("Eggs")
print(ss.sheetTitles)   #追加されたシートも表示されているはず

ss.createSheet("Bacon", 0)
print(ss.sheetTitles)   #追加された「Bacon」が先頭に表示されているはず

#シート1のセルになにか入れておく
sheet = ss["シート1"]
sheet["A1"] = "Sheet1-A1"

sheet = ss["Eggs"]
sheet.delete()  #Eggsシートだけ消す
print(ss.sheetTitles)   #Eggsシートはもうない

ss["シート1"].clear()  #シート削除でなく「消去」

