print("外にでかけたいです。")
print("雨が降っていますか？ (y/n)>", end='')
tenki=input()
if tenki == 'y':    #雨が降っている
    print("傘を持っていますか？ (y/n)>")
    kasa=input()
    if kasa == 'y': #傘がある
        print("出かける")
    else:   #傘がない
        print("少し待ちます…")
        print("まだ振りそうですか？ (y/n)>")
        mada=input()
        if mada=='y':   #まだ降ってる
            print("あきらめました")
        else:   #やんだみたい
            print("やっと出かけられます")
else:    #雨が降っていない
    print("いってきます！")