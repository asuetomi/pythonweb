'''
「exit」と入力して終了するまで、無限に入力した値を足し続けるプログラムを作成して下さい。
'''
count = 0

while True:
    print("count = ", count)
    indata = input("入力して下さい（exitで終了）：")
    if str(indata) == "exit":
        break
    count += int(indata)
print("last count = ", count)