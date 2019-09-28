'''
以下のものを作成してください。
1. キーを入力して下さい、と表示して値を入力させる
2. バリューを入力して下さい、と表示して値を入力させる
3. 入力結果を辞書に登録していく
4. 辞書を表示する
5. 1 に戻る
6. 途中で exit と入力されたら終了する
'''
dic = {}
while True:
    key = input("キーを入力して下さい: ")
    if key == "exit":
        break
    value = input("バリューを入力して下さい: ")
    if value == "exit":
        break
    dic[key] = value
    print(dic)
print(dic)
