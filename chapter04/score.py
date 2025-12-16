#成績の入力

#リスト
name=["相沢いわし","伊藤うずら","上野えのき"]
score=[0,0,0]

#成績の入力
for i in range(3):
    score[i]=int(input(f"{name[i]}さんの点数を入力してください >>"))

#成績の表示
for i in range(3):
    print(f"{name[i]}さん：{score[i]}点")

#こんな入力部の書き方もある--------------------------------
"""
number=0
for i in name:
    score[number]=int(input(f"{i}さんの点数を入力してください >>"))
    number+=1
"""
