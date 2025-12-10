import random, sys

#勝ち/負け/あいこのカウント
wins = 0
loses = 0
ties = 0

#ゲーム開始
while True: #ゲームのループ
    print(f"{wins}勝 {loses}敗 あいこ{ties}回")

    while True: #入力のループ
        player_move = int(input("グー：0、チョキ：1、パー：2、ゲーム終了：3 ->"))
        if player_move == 3:
            sys.exit()  #プログラム終了
        if player_move >= 0 and player_move <= 2:
                break   #勝ち負けの判定に行く
        print("0から3までの数字を入力してくださいね")
    #入力のループここまで

    #コンピュータは人間の手をあえて見ないようにして出す手を後出ししている
    computer_move = random.randint(0, 2)
    #勝敗の判定
    if computer_move == player_move:    #まずはあいこ
        print("あいこです")
        ties += 1
    else:   #勝ちか負けのパターン
        if computer_move == 0:    #コンピュータがグーの場合
            print("コンピュータ：グー　", end="")
            if player_move == 1:  #人間はチョキ
                print("あなた：チョキ …あなたの負けです")
                loses += 1
            else:  #人間はパー
                print("あなた：パー …あなたの勝ちです")
                wins += 1
        elif computer_move == 1:    #コンピュータがチョキの場合
            print("コンピュータ：チョキ　", end="")
            if player_move == 0:  #人間はグー
                print("あなた：グー …あなたの勝ちです")
                wins += 1
            else:   #人間はパー
                print("あなた：パー …あなたの負けです")
                loses += 1
        else:   #コンピュータがパーの場合
            print("コンピュータ：パー　", end="")
            if player_move == 0:  #人間はグー
                print("あなた：グー …あなたの負けです")
                loses += 1
            else:   #人間はチョキ
                print("あなた：チョキ …あなたの勝ちです")
                wins += 1
#ゲームのループここまで
