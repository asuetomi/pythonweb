'''
辞書ファイルがあれば読み込んで、入力内容を辞書に追加していくプログラム
'''
import os

filename = "dictest2.txt"
dic = {}

if os.path.exists(filename):
    with open(filename) as openfile:
        data = openfile.read()
        lines = data.splitlines()
        for line in lines:
            keyvalue = line.split(":")
            dic[keyvalue[0]] = keyvalue[1]

print(dic)

while True:
    key = input("何か言って ")
    if key == "おしまい":
        break
    if key in dic:
        print(dic[key]," のことですね")
    else:
        value = input("それはどういう意味？ ")
        print(key," は ",value," のことですね")
        dic[key] = value

print("さよなら")
with open(filename,"w") as openfile:
    for key in dic.keys():
        openfile.writelines(key+":"+dic[key]+"\n")

print(dic)
