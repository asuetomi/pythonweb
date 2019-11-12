import MySQLdb

db_config = {
    'host':'localhost',
    'db':'suetomi',
    'user':'a_sue',
    'passwd':'password',
    'charset':'utf8',
}

dicfilename = "talkdic.csv"
responsefilename = "response.csv"
# siritoriFilename = "siritori.csv"
siritoriFilename = "C:/Users/a_sue/OneDrive/workspace/PythonLearn/pubdic+-wnn/utf-8/words.csv"

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


try:
    conn = MySQLdb.connect(host=db_config['host'], db=db_config['db'], user = db_config['user'],
                          passwd=db_config['passwd'], charset=db_config['charset'])
    cursor = conn.cursor()
    cursor.execute('SELECT * from test')
    # cursor.execute("INSERT INTO words (word, mean) VALUES ('あいうえお', 'かきくけこ');")
    # dic = loadDic(dicfilename)
    # for key in dic:
    #     print("INSERT INTO words (word, mean) VALUES ('" + key + "', '"+ dic[key] +"');")
    #     cursor.execute("INSERT INTO words (word, mean) VALUES ('" + key + "', '"+ dic[key] +"');")
    # #     # cursor.execute("INSERT INTO words (word, mean) VALUES ('%s', '%s');", key, dic[key])
    # #     cursor.execute("INSERT INTO words (word, mean) VALUES ('あいうえお', 'かきくけこ');")
    # cursor.execute("commit;")

    # rdic = loadDic(responsefilename)
    # for key in rdic:
    #     if key != "":
    #         cursor.execute("INSERT INTO response(keyword, text) VALUES ('" + key + "', '"+ rdic[key] +"')")
    # cursor.execute("commit;")

    sdic = loadDic(siritoriFilename)
    # for key in sdic:
    #     if key != "":
    #         for word in sdic[key].split("|"):
    #             if word != "":
    #                 cursor.execute("INSERT INTO siritori(ruby) VALUES ('" + word + "')")
    for key in sdic:
        if key != "":
            cursor.execute("INSERT INTO siritori(ruby, word) VALUES ('" + key  + "', '"+ sdic[key] +"')")
    cursor.execute("commit;")

    
    print(cursor.rowcount)
    print(cursor.fetchall())
except MySQLdb.Error as ex:
    print('MySQL Error:', ex)