#あいさつする関数
def aisatsu(namae, jikantai):
    if jikantai == 1:
        print(f"{namae}さん、おはようございます")
    elif jikantai == 2:
        print(f"{namae}さん、こんにちは")
    elif jikantai == 3:
        print(f"{namae}さん、こんばんは")
    else:
        print(f"{namae}さん、おやすみなさい")
    #関数aisatsuはここまで

#プログラム実行はここから
name = input("名前を入力して下さい >>")
print("朝：1 昼：2 晩：3 寝る前：4")
jikan = int(input("時間帯を入力してください >>"))
aisatsu(name,jikan)
