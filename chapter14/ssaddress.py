import ezsheets

print(ezsheets.convertAddress("A2"))    #画面上のアドレス->タブル型のアドレス
print(ezsheets.convertAddress(1,2)) #タプル型のアドレス->画面上のアドレス
print(ezsheets.getColumnLetterOf(2))    #数字の列->文字型の列
print(ezsheets.getColumnNumberOf('B'))  #文字型の列->数字の列
print(ezsheets.getColumnLetterOf(999))  #数字の列->文字型の列
print(ezsheets.getColumnNumberOf("ZZZ"))    #文字型の列->数字の列(最大列)
