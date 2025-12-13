import random,time

#関数casper
def casper():
    kekka = random.randint(1,100)
    mati=random.randint(1,3)
    time.sleep(mati)
    if kekka <= 50:
        print("Casper … 可決")
        return 0
    else:
        print("Casper … 否決")
        return 1

#関数balthasar
def balthasar():
    kekka = random.randint(1,100)
    mati=random.randint(1,3)
    time.sleep(mati)
    if kekka % 2 == 1:
        print("Balthasar … 可決")
        return 0
    else:
        print("Balthasar … 否決")
        return 1

#関数melchior
def melchior(agenda):
    kekka = random.randint(1,100)
    mati=random.randint(1,3)
    time.sleep(mati)
    nagasa=len(agenda)
    if nagasa%2 == 1:   #casperと同じ
        if kekka <= 50:
            print("Melchior … 可決")
            return 0
        else:
            print("Melchior … 否決")
            return 1
    else:   #casperとは逆
        if kekka <= 50:
            print("Melchior … 否決")
            return 1
        else:
            print("Melchior … 可決")
            return 0

#プログラムここから
gidai=input("議題はなんですか >>")
print("[審議中]")
#各関数を呼び出す(＆多数決を取る)
result=casper()+balthasar()+melchior(gidai)
#結果表示
#resultがゼロ…可決,1…可決,2…否決,3…否決
print("[決議]")
if result > 1:
    print(f"議題「{gidai}」は否決されました")
else:
    print(f"議題「{gidai}」は可決されました")
#プログラム終了
