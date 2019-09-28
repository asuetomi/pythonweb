'''
辞書データをワークファイルに書き込み、そのデータを辞書データに読み込み直すプログラムを作成しましょう。
'''
filename = "dictest.txt"

dic = {"春":"spring", "夏":"summer", "秋":"autumn", "冬":"winter",}
print(dic)
with open(filename,"w") as openfile:
    for key in dic.keys():
        openfile.writelines(key+":"+dic[key]+"\n")

dic2 = {}
with open(filename) as openfile:
    # for data in openfile:
    #     keyvalue = data.split(":")
    #     dic2[keyvalue[0]] = keyvalue[1].replace("\n","")
    data = openfile.read()
    print(data)
    lines = data.splitlines()
    # print(lines[0])
    print(lines)
    for line in lines:
        keyvalue = line.split(":")
        dic2[keyvalue[0]] = keyvalue[1]

print(dic2)
