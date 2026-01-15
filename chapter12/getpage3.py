import requests

url=input("URLを指定してください>>")
ext=int(input("抽出文字数を入力して下さい>>"))
res=requests.get(url)
try:
    res.raise_for_status()
except Exception as  exc:
    print(f"問題あり：{exc}")
print(res.text[:ext])
