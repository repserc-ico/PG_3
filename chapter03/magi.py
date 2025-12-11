import random,time

#関数casper
def casper():
    kekka = random.randint(0,1)
    mati=random.randint(1,3)
    time.sleep(mati)
    if kekka == 0:
        print("Casper … 可決")
    else:
        print("Casper … 否決")
    return kekka

#関数balthasar
def balthasar():
    kekka = random.randint(0,1)
    mati=random.randint(1,3)
    time.sleep(mati)
    if kekka == 0:
        print("Balthasar … 可決")
    else:
        print("Balthasar … 否決")
    return kekka

#関数melchior
def melchior():
    kekka = random.randint(0,1)
    mati=random.randint(1,3)
    time.sleep(mati)
    if kekka == 0:
        print("Melchior … 可決")
    else:
        print("Melchior … 否決")
    return kekka

#プログラムここから
gidai=input("議題はなんですか >>")
print("[審議中]")
#各関数を呼び出す(＆多数決を取る)
result=casper()+balthasar()+melchior()
#結果表示
#resultがゼロ…可決,1…可決,2…否決,3…否決
print("[決議]")
if result > 1:
    print(f"議題「{gidai}」は否決されました")
else:
    print(f"議題「{gidai}」は可決されました")
#プログラム終了
