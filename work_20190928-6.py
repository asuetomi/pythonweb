'''
 1. 辞書をファイルに入れる。
 2. ファイルを辞書に入れる。
 3. 入力待ちをする。
 4. 入力されたものが辞書になければ「（入力された内容）って何ですか？」と質問する。
 5. 回答を入力待ちする。
 6. 質問と答えを辞書に入れ、ファイルに記録する。
 7. 1に戻る。
 8． in 演算子を使用して、文章中に「こんにちは」がふくまれていたら、挨拶を返しましょ う
 9. ランダム応答用のファイルを別に用意して挨拶をされたら、挨拶を返した後に応答 用ファイルから話題を提供できるようにしましょう
10. しりとり、と入力された場合、しりとりを開始しましょう。
    最後に「ん」がつく言葉が来た ら勝敗判定しましょう。
    また、コンピュータが分からない言葉が来たら負けとして、その言葉にどう返せばいいか聞きましょう。
    聞いた言葉はファイルに記録して、徐々に成⾧させましょう。
11. しりとりで、一度出た言葉を使用できないようにしましょう
'''

import random

dicfilename = "talkdic.csv"
responsefilename = "response.csv"
siritoriFilename = "siritori.csv"
dic = {}

def saveDic(filename, dic):
    '''辞書をファイルにCSV形式で保存する
    '''
    with open(filename, "w", encoding="utf-8") as f:
        for key in dic:
            f.write(key + "," + dic[key] + "\n")

def loadDic(filename):
    '''ファイルに保存された辞書を読み出してdict型を返す
    '''
    rtdic ={}
    with open(filename, "r", encoding="utf-8") as fr:
        readdata = fr.read()
        lines = readdata.splitlines()
        for line in lines:
            data = line.split(",")
            rtdic[data[0]] = data[1]
    return rtdic

def siritori():
    '''しりとりをする
    '''
    siriDic = loadDic(siritoriFilename)
    print("しりとりをするのね。お先にどうぞ")
    res = ""
    while(True):
        ret = input(res + " > ")
        while (res != "" and ret[0] != res[-1]):
            print("ちがうよ")
            ret = input(res + " > ")
            continue
    # 最後に「ん」がつく言葉が来た ら勝敗判定しましょう。また、コンピュータが分からない言葉が来たら負けとして、その 言葉にどう返せばいいか聞きましょう。聞いた言葉はファイルに記録して、徐々に成 ⾧させましょう。
        if ret[-1] == "ん":
            print("「ん」で終わったからあなたの負けです。")
            break
        ans = siriDic[ret[-1]].split("|")
        print(ans, len(ans), "[" + ans[0] + "]")
        if len(ans) == 1 and ans[0] == "":
            print("う～ん、わかりません。私の負けです")
            break
        res = ans[random.randint(0, len(ans) - 1)]
    return



# ファイルがないときのため
with open(dicfilename, "a") as f:
    pass

#  2. ファイルを辞書に入れる。
dic = loadDic(dicfilename)

# 応答用ファイルを読む
resDic = loadDic(responsefilename)
# print(resDic)
resMax = len(resDic) - 1
# print(resMax)
with open(dicfilename, "a", encoding="utf-8") as f:
    while True:
    #  3. 入力待ちをする。
        key = input("何か言って ")
        if key == "exit":
            break
    #  8． in 演算子を使用して、文章中に「こんにちは」がふくまれていたら、挨拶を返しましょ う
        if "こんにちは" in key:
            print("こんにちは")
    #  9. ランダム応答用のファイルを別に用意して挨拶をされたら、挨拶を返した後に応答 用ファイルから話題を提供できるようにしましょう
            key = input(resDic[str(random.randint(0, resMax))])
    # 10. しりとり、と入力された場合、しりとりを開始しましょう。
        if "しりとり" in key:
            siritori()
            continue
        if key in dic:
            print(dic[key]," のことですね")
        else:
    #  4. 入力されたものが辞書になければ「（入力された内容）って何ですか？」と質問する。
    #  5. 回答を入力待ちする。
            value = input(key + "って何ですか？ ")
            print(key," は ",value," のことですね")
    #  6. 質問と答えを辞書に入れ、ファイルに記録する。
            dic[key] = value
            # saveDic(dicfilename, dic)
            f.write(key + "," + dic[key] + "\n")

print("またね")
