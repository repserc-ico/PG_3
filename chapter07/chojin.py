import re

text = input("あなたが知っている超人は？ >>")

#複数のパターンから選んでマッチする
chojin_regex = re.compile(r'.*(ウー)?マン|.*([wW][oO])?[mM][aA][nN]')
mo = chojin_regex.search(text)
if mo.group() != None:
    print(f"{mo.group()}参上！")
else:
    print("そんなのいません")