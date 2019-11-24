from django.db import models
from . models import words
# import . views

dic = []

def chat(params:dict):
    if 'chat' == params['mode']:
        key = params['txt']

        # my_dict['txt'] = key
        # params['prompt'] = key + "ってなに？"
        # params['mode'] = 'chat'
        # return params

    #  3. 入力待ちをする。
        # key = input("何か言って > ")
        # if key == "exit":
        #     break
        # if key == "":
        #     continue
    #  8． in 演算子を使用して、文章中に「こんにちは」がふくまれていたら、挨拶を返しましょ う
        if "こんにちは" in key:
            # print("こんにちは")
            params['prompt'] = "こんにちは"
            return params
    #  9. ランダム応答用のファイルを別に用意して挨拶をされたら、挨拶を返した後に応答 用ファイルから話題を提供できるようにしましょう
            key = input(resDic[str(random.randint(0, resMax))])
    # 10. しりとり、と入力された場合、しりとりを開始しましょう。
        if "しりとり" in key:
            siritori()
            # continue
        # if key in dic:

        try:
            word = words.objects.get(word = key)
            params['prompt'] = word.mean + " のことですね"
            return params
            pass
        except:
    #  4. 入力されたものが辞書になければ「（入力された内容）って何ですか？」と質問する。
    #  5. 回答を入力待ちする。
            params['prompt'] = key + "って何ですか？ "
            params['mode'] = 'answer'
            return params
            value = input(key + "って何ですか？ ")
            print(key," は ",value," のことですね")
    #  6. 質問と答えを辞書に入れ、ファイルに記録する。
            dic[key] = value
            # saveDic(dicfilename, dic)
            f.write(key + "," + dic[key] + "\n")
    elif 'answer' == params['mode']:
        key = params['txt']
        params['lines'].append(params['prompt'])
        word = words(word = params['prompt'].replace("って何ですか？", ""), mean = params['txt'])
        word.save()
        params['lines'].append(word.mean + " のことですね")
        
        params['prompt'] = "何か言って？"
        params['mode'] = 'chat'
        return params


