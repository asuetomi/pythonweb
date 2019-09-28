'''
1. 英和辞書を dict型で作成し、
2. 辞書をファイルにCSV形式で保存
3. ファイルに保存された辞書を読み出してdict型の変数に入れる
'''
filename = "ejdic.csv"
ejdic = {
    "spring":"春",
    "summer":"夏",
    "autumn":"秋",
    "winter":"冬",
}

with open(filename, "w", encoding="utf-8") as f:
    for key in ejdic:
        f.write(key+","+ejdic[key]+"\n")

ejdic2 ={}
with open(filename, "r", encoding="utf-8") as fr:
    readdata = fr.read()
    lines = readdata.splitlines()
    for line in lines:
        dic = line.split(",")
        ejdic2[dic[0]] = dic[1]

print(ejdic2)

