#星座占い その２

#リスト
name=["","山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座",
      "蟹座","獅子座","乙女座","天秤座","蠍座","射手座","山羊座"
]
keyword=['','"I keep ..."(私は守る)','"I solve ..."（私は解明する)','"I believe ..."（私は信じる)',
         '"I exist."(私は存在する)','"I have ..."(わたしは所有する)','"I choose ..."(私は選択する)',
         '"I sense ..."（私は感じる)','"I will ..."(私は～する)','"I analyze ..."（私は分析する)',
         '"I balance ..."（私はバランスをとる)','"I want ..."(私は要求する)','"I experience ..."(私は体験する)',
         '"I keep ..."(私は守る)',
]
slip=[0,20,19,21,20,21,22,23,23,23,24,23,22]
#誕生月日を入力
month=int(input("誕生月を入力してください >>"))
day=int(input("誕生日を入力してください >>"))

#星座を特定
seiza=month #その月の星座として仮決定
for i in range(1,13):
    if month==i and day>=slip[i]:
        seiza+=1

#表示
print(f"あなたの星座は{name[seiza]}です")
print(f"キーワードは{keyword[seiza]}です")
