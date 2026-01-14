#数当てゲーム
import random
secret_number = random.randint(1, 20)
print("1から20までの数を当てましょう")

#6回聞く
for guesses_taken in range(1, 7):
    #print("数を入力してください")
    #guess=int(input())
    guess = int(input("数を入力してください->"))
    if guess < secret_number:
        print("あなたの推定値は小さいです")
    elif guess > secret_number:
        print("あなたの推定値は大きいです")
    else:
        break

if guess == secret_number:
    #print("当たり！"+str(guesses_taken)+"回で当たりました！")
    print(f"当たり！{guesses_taken}回で当たりました！")
else:
    #print("残念。正解は"+str(secret_number)+"でした")
    print(f"残念。正解は{secret_number}でした")
