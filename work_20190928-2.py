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

def writeDic(dic):
    '''辞書をファイルにCSV形式で保存する
    '''
    with open(filename, "w") as f:
        for key in dic:
            f.write(key + "," + dic[key] + "\n")

def readDic():
    '''ファイルに保存された辞書を読み出してdict型を返す
    '''
    rtdic ={}
    with open(filename, "r") as fr:
        readdata = fr.read()
        lines = readdata.splitlines()
        for line in lines:
            dic = line.split(",")
            rtdic[dic[0]] = dic[1]
    return rtdic

if __name__ == "__main__":
    ejdic2 = {}
    writeDic(ejdic)
    ejdic2 = readDic()
    print(ejdic2)

