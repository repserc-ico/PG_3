#Yahooニュースのヘッドラインを抽出
from urllib import request
from bs4 import BeautifulSoup

url="https://news.yahoo.co.jp/topics"

#指定URLの表示内容をざっくり取得
response = request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
response.close()

#ヘッドラインを抽出
news_text = soup.find("div", "sc-hwj2au-0")

#タグを削除して表示　※全部１行で表示されてしまう＞＜
#news_text = news_text.get_text()

#aタグごとにヘッドラインを取り出すようにする
for element in news_text.find_all('a'):
    if element.text == "もっと見る":
        print("")
    else:
        print(element.text)