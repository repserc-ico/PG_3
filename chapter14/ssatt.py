import ezsheets
#スプレッドシートのタイトルは「Title of New Spreadsheet」にしておく
#スプレッドシート内に「Students」「Classes」「Resources」の３つのシートを作っておく(中身はなくていい)

#スプレッドシートのIDについてはテキストp418下段を参照のこと
ss = ezsheets.Spreadsheet("17bNuLb6mbSg9jF06btkqfngnlDdsLlK3buttNCIyVY0")
print(ss.title)

ss.title = "Class Data" #書き込み許可がなければエラー

print(ss.spreadsheetId) #シートのID
print(ss.url)   #シートのURL
print(ss.sheetTitles)   #各シートのタイトル一覧
print(ss.sheets)    #各シートの情報一覧

#各シートはリスト番号でもシート名でも取得可能
print(ss[0])
print(ss["Students"])

del ss[0]   #リストの要素を削除という扱い
print(ss.sheetTitles)   #各シートのタイトル一覧
#もうStudentシートはない

ss.refresh()
