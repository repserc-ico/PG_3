#テキストp270 都道府県クイズの問題と解答を35個つくる
#でも、35個つくるのは大変だからつくる数を指定できるようにしました
import random

#問題のデータ(辞書形式)
capitals = {
    "北海道":"札幌市", "青森県":"青森市", "岩手県":"盛岡市", "宮城県":"仙台市", "秋田県":"秋田市",
    "山形県":"山形市", "福島県":"福島市", "茨城県":"水戸市", "栃木県":"宇都宮市", "群馬県":"前橋市",
    "埼玉県":"さいたま市", "千葉県":"千葉市", "東京都":"新宿区", "神奈川県":"横浜市", "新潟県":"新潟市",
    "富山県":"富山市", "石川県":"金沢市", "福井県":"福井市", "山梨県":"甲府市", "長野県":"長野市",
    "岐阜県":"岐阜市", "静岡県":"静岡市", "愛知県":"名古屋市", "三重県":"津市", "滋賀県":"大津市",
    "京都府":"京都市", "大阪府":"大阪市", "兵庫県":"神戸市", "奈良県":"奈良市", "和歌山県":"和歌山市",
    "鳥取県":"鳥取市", "島根県":"松江市", "岡山県":"岡山市", "広島県":"広島市", "山口県":"山口市",
    "徳島県":"徳島市", "香川県":"高松市", "愛媛県":"松山市", "高知県":"高知市", "福岡県":"福岡市",
    "佐賀県":"佐賀市", "長崎県":"長崎市", "熊本県":"熊本市", "大分県":"大分市", "宮崎県":"宮崎市",
    "鹿児島県":"鹿児島市", "沖縄県":"那覇市"
}

#問題集を作成する数を設定
issue = int(input("問題集を作成する数を指定して下さい>>") )

#問題集を作成する
for quiz_num in range(issue):
    #問題集と回答集のファイルを作成
    quiz_file = open(f"capitalquiz{quiz_num + 1}.txt", "w")
    answer_key_file = open(f"capitalquiz_answers{quiz_num + 1}.txt", "w")
    #問題集のヘッダーを出力
    quiz_file.write(f"名前：\n\n日付：\n\n学期：\n\n")
    quiz_file.write((' '*20)+f"都道府県所在地クイズ：問題番号{quiz_num + 1}\n\n")
    #解答のヘッダーを出力
    answer_key_file.write(f"問題番号{quiz_num + 1}の解答\n\n")
    #都道府県の順番をシャッフルする
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)
    #47都道府県をループしてそれぞれ問題を作成する
    for question_num in range(len(prefectures)):
        #正答と誤答を抽出する
        correct_answer = capitals[ prefectures[question_num] ]  #正解の庁所在地
        wrong_answers = list(capitals.values() ) #まず庁所在地だけをリストに抽出
        del wrong_answers[wrong_answers.index(correct_answer) ] #正解の庁所在地だけ除去
        wrong_answers = random.sample(wrong_answers, 3) #不正解の選択肢を３つだけ抽出
        answer_options = wrong_answers + [correct_answer]   #不正解と正解の選択肢を合わせる(4択になる)
        random.shuffle(answer_options)  #選択肢をシャッフルする
        #問題文と解答の選択肢を問題ファイルに出力する
        quiz_file.write(f"{question_num + 1}. ")    #問題番号
        quiz_file.write(prefectures[question_num] ) #都道府県名
        quiz_file.write("の都道府県庁所在地は？\n")    #問題文ここまで
        for i in range(4):  #4択の選択肢を出力
            quiz_file.write(f' {"ABCD"[i]}. {answer_options[i] }\n') #選択肢ひとつずつ
        quiz_file.write("\n")   #問題文の区切りの空行
        #答えの選択肢を解答ファイルに出力する
        answer_key_file.write(f"{question_num + 1}. ") #問題番号
        answer_key_file.write("ABCD"[answer_options.index(correct_answer) ] ) #正解インデックス番号の選択肢だけ
        answer_key_file.write("\n") #解答の区切りの改行
    #47問題の処理が終わったら問題文と解答のファイルそれぞれをクローズする
    quiz_file.close()
    answer_key_file.close()
    #ひとり分の問題作成処理終わり

#全員分の問題作成処理終わり
print(f"{issue}人ぶんの問題と解答を作成しました。")