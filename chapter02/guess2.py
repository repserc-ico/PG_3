#数当てゲーム
import random
print("1から10までの数を当てましょう")
score = 5
game = 1
while True:
    print(f"*** GAME {game} ***")
    secret_number = random.randint(1, 10)
    #10回聞く
    for guesses_taken in range(1, 11):
        guess = int(input("数を入力してください(ゼロは終了)->"))
        if guess == 0:
            break
        if guess < secret_number:
            print("あなたの推定値は小さいです")
            score -= 1
        elif guess > secret_number:
            print("あなたの推定値は大きいです")
            score -= 1
        else:
            print("なんと！正解！")
            score += 10
            game += 1   #次のゲーム開始
            break
    if guess == 0:  #終了を選択した時だけ抜ける
        break

#結果発表
print(f"正解は{secret_number}でした")
print(f"得点は{score}点でした")

