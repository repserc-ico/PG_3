#沖縄の○○

#辞書のデータ
okinawa={"県花":"デイゴ", "県鳥":"ノグチゲラ", "県魚":"タカサゴ",
         "県のお菓子":"こんぺん", "ソウルフード":"沖縄そば"}

#キーの一覧表示
print(okinawa.keys())

#調べたいものを入力
search=input("調べたいものはなんですか >>")

#キーに対するバリューを表示する
if search in okinawa:
    print(okinawa[search])
else:
    print("そのデータはありません")