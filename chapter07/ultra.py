import re

text = input("光の国からやってきた…？ >>")

#複数のパターンから選んでマッチする
chojin_regex = re.compile(r'^ウルトラ.*|^[uU][lL][tT][rR][aA].*')
mo = chojin_regex.search(text)
if mo.group() != None:
    print(f"{mo.group()}参上！")
else:
    print("そんなのいません")