#青空文庫からタグを省いて出力　※一部エラーあり
from urllib import request
from bs4 import BeautifulSoup

url=["", "https://www.aozora.gr.jp/cards/000148/files/752_14964.html",
     "https://www.aozora.gr.jp/cards/000879/files/95_15247.html",
     "https://www.aozora.gr.jp/cards/000081/files/473_42318.html",
     "https://www.aozora.gr.jp/cards/000129/files/45244_22341.html",
     "https://www.aozora.gr.jp/cards/001030/files/4803_14204.html",
]

print("[[[ 青空文庫より ]]]")
print("1. 夏目漱石")
print("2. 芥川龍之介")
print("3. 宮沢賢治")
print("4. 森鴎外")
print("5. 堀辰雄")

book=int(input("誰の作品にしますか(1-5)>>"))

#指定URLの表示内容をざっくり取得
response = request.urlopen(url[book])
soup = BeautifulSoup(response)
response.close()
#print(soup)    #青空文庫のページ内容そのもの

#作品タイトルから本文のみを抽出
main_text = soup.find('div', class_='main_text')
#rpタグとrtタグを削除する
tags_to_delete = main_text.find_all(['rp', 'rt'])
for tag in tags_to_delete:
    tag.decompose()

#get_textメソッドを使用してタグを削除
main_text = main_text.get_text()

#余計なコードを除去
main_text = main_text.replace('\r', '').replace('\u3000', '')
print(main_text)

#取得したテキストを改行ごとに１要素としてリストに格納することもできる
#text_list = main_text.splitlines()
#print(text_list)
