# -*- coding: utf-8 -*-
import logging
import sys
from gensim.corpora import WikiCorpus
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
'''
    extract data from wiki dumps(*articles.xml.bz2) by gensim.
    @chenbingjin 2016-05-11
'''
def help():
    print ("传入参数不足，请使用python process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.txt传入待处理的文件和保存的文件名")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        sys.exit(1)
    logging.info("running %s" % ' '.join(sys.argv))
    inp, outp = sys.argv[1:3]
    i = 0

    output = open(outp, 'w',encoding='utf-8')
    wiki = WikiCorpus(inp, dictionary={})
    for text in wiki.get_texts():
        output.write(" ".join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logging.info("已完成 "+str(i) + " 条数据")
    output.close()
    logging.info("全部完成，共生成了 "+str(i) +" 条数据")