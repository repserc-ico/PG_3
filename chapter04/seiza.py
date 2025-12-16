#星座占い その１

#リスト
name=["","山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座",
      "蟹座","獅子座","乙女座","天秤座","蠍座","射手座",
]
keyword=['','"I keep ..."(私は守る)','"I solve ..."（私は解明する)','"I believe ..."（私は信じる)',
         '"I exist."(私は存在する)','"I have ..."(わたしは所有する)','"I choose ..."(私は選択する)',
         '"I sense ..."（私は感じる)','"I will ..."(私は～する)','"I analyze ..."（私は分析する)',
         '"I balance ..."（私はバランスをとる)','"I want ..."(私は要求する)','"I experience ..."(私は体験する)',
]
#誕生月日を入力
month=int(input("誕生月を入力してください >>"))
day=int(input("誕生日を入力してください >>"))

#星座を特定
seiza=month #その月の星座として仮決定
if month==1 and day>=20:
    seiza+=1
elif month==2 and day>=19:
    seiza+=1
elif month==3 and day>=21:
    seiza+=1
elif month==4 and day>=20:
    seiza+=1
elif month==5 and day>=21:
    seiza+=1
elif month==6 and day>=22:
    seiza+=1
elif month==7 and day>=23:
    seiza+=1
elif month==8 and day>=23:
    seiza+=1
elif month==9 and day>=23:
    seiza+=1
elif month==10 and day>=24:
    seiza+=1
elif month==11 and day>=23:
    seiza+=1
elif month==12 and day>=22:
    seiza=1
#表示
print(f"あなたの星座は{name[seiza]}です")
print(f"キーワードは{keyword[seiza]}です")
