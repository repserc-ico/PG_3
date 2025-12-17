#数占い(数秘術)

#生年月日を文字列として入力
year = str(input("生まれた年はいつですか >>"))
month = str(input("生まれた月はいつですか >>"))
day = str(input("生まれた日はいつですか >>"))

number=0

for i in year:
    number += int(i)
    #これと同じ
    #number = int(year[0]) + int(year[1]) + int(year[2]) + int(year[3])
for i in month:
    number += int(i)
for i in day:
    number += int(i)

while number>=10:
    tmp=str(number)
    number = 0  #いったんクリア
    for i in tmp:
        number += int(i)

print(f"あなたの運命数は{number}です")