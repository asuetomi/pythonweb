count = 1
print("5回まで入力できます。")
while count < 6:
    data = input("入力して下さい > ")
    print(count,"回目=",data)
    if data == "exit":
        break
    count += 1
if count <6:
    print("途中で止めました")
    print(count,"回目で止めました")
else:
    print("5回入力しました")
