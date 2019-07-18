from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import sqlite3
import jieba
import pandas as pd
import pyhdfs

def huabanlearn(search):
    # client = pyhdfs.HdfsClient("10.8.161.29","9000","zxf")
    # a = client.open("/b.txt")
    # print(a.read())
    conn = sqlite3.connect("/home/zxf/zz1806/zz1806/untitled6/db.sqlite3")
    huabans = pd.read_sql("select * from huaban",conn)
    huaban_data = []
    huaban_target = []

    results = huabans.loc[:, ["imgdiscrit", "name"]]
    for i in range(results.shape[0]):
        cut_data = jieba.cut(results["imgdiscrit"][i])

        cut_result = ' '.join(list(cut_data))
        huaban_data.append(cut_result)
        huaban_target.append(results["name"][i])
    # print(huaban_data)

    tfidf = TfidfVectorizer()
    x_tfidf = tfidf.fit_transform(huaban_data)
    clf = MultinomialNB(alpha=1.0).fit(x_tfidf,huaban_target)

    huaban = []
    huaban.append(search)
    x_tfidf = tfidf.transform(huaban)
    predicted = clf.predict(x_tfidf)
    return predicted
# print(huabanlearn('可爱'))







