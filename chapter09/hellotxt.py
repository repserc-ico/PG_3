#指定したファイルを読み込んで中身を表示
hello_file = open("hello.txt")

#読み込んだ中身を表示
print(hello_file.read())
#読み込んだ中身を１行ずつ取得してリストにセットして表示
#print(hello_file.readlines())