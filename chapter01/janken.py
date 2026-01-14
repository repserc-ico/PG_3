#じゃんけん
import random, sys

#勝ち負けあいこの数を記録
wins = 0
loses = 0
ties = 0

while True:
    print(f"{wins}勝 {loses}敗 あいこ{ties}回")
    while True:
        player_move = input("(r)ock, (p)aper, (s)cissors or (q)uit ->")
        if player_move == "q":
            sys.exit()  #プログラム終了
        if player_move == "r" or player_move == "p" or player_move == "s":
            break   #勝ち負けの判定に行く
        print("「r」か「p」か「s」か「q」を入力してください")

    if player_move == "r":
        print("グー 対 ...")
    elif player_move == "p":
        print("パー 対 ...")
    else:
        print("チョキ 対 ...")
    #コンピュータの手を表示
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print("グー")
    elif random_number == 2:
        computer_move = 'p'
        print("パー")
    else:
        computer_move = 's'
        print("チョキ")

    #勝負判定
    if player_move == computer_move:
        print("あいこです！")
        ties += 1
    #勝ちパターン
    elif player_move == "r" and computer_move == "s":
        print("あなたの勝ち！")
        wins += 1
    elif player_move == "p" and computer_move == "r":
        print("あなたの勝ち！")
        wins += 1
    elif player_move == "s" and computer_move == "p":
        print("あなたの勝ち！")
        wins += 1
    #負けパターン
    elif player_move == "r" and computer_move == "p":
        print("あなたの負け")
        loses += 1
    elif player_move == "p" and computer_move == "s":
        print("あなたの負け")
        loses += 1
    elif player_move == "s" and computer_move == "r":
        print("あなたの負け")
        loses += 1