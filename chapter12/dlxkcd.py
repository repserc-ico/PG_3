# dlxkcd.py テキストp351ページ以降を参照
# ※プログラムのあるディレクトリ下にxkcdディレクトリが作られ、
# 　画像がダウンロードされます(xkcdディレクトリはGitHubにadd不要です)

import requests, os, bs4
url="https://xkcd.com/"
os.makedirs("xkcd", exist_ok=True)
while not url.endswith('#'):
    #ページをダウンロードする
    print(f"ページをダウンロード中 {url}…")
    res = requests.get(url) #Webページをダウンロード
    res.raise_for_status()  #アクセスエラーのチェック
    soup = bs4.BeautifulSoup(res.text, "html.parser")    #HTML解析できる形式に変換
    #コミック画像のURLを見つける
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("コミック画像が見つかりませんでした")
    else:
        comic_url = "https:" + comic_elem[0].get("src") #画像ファイルのURLを取得
        #画像をダウンロードする
        print(f"画像をダウンロード中 {comic_url}…")
        res = requests.get(comic_url) #画像ファイルのダウンロード
        res.raise_for_status() #アクセスエラーのチェック
        #画像を./xkcdに保存する
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")  #PCのファイルを書き込みオープン
        for chunk in res.iter_content(100000):  #およそ100Kバイトごとに読み込む
            image_file.write(chunk) #ファイルに書き込み
        image_file.close()  #ファイルをクローズする
    #「Prev」ボタンのURLを取得する
    prev_link = soup.select("a[rel='prev']")[0] #Prevボタンのリンクの情報を取得
    url = "https://xkcd.com" + prev_link.get("href")    #リンクの情報が”/3172/”となってるのでフルアドレスに編集

print("完了")