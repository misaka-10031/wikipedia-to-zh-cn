import jieba
import sys
from matplotlib import lines
from sympy import finite_diff_weights
from tqdm import tqdm

def cutIt(inputFileName,outputFileName):
    output = open(outputFileName,'w',encoding='utf8')
    finish = 0
    seg_list = jieba.cut("正在加载分词数据")  # 避免进度条被阻断
    print(" ".join(seg_list))
    with open(inputFileName,'r',encoding='utf8') as lines:
        print ('正在载入文件，视文件大小及计算机性能，可能需要10秒到几分钟...')
        for i in enumerate(lines):
            finish += 1
    with open(inputFileName,'r',encoding='utf8') as source:
        line = source.readline()
        count = 0
        with tqdm(total=finish, desc='分词进度', leave=False, unit='line') as pbar:
            for i in range(0,finish):
                sentence = ''
                count += 1
                for w in jieba.cut(line):
                    sentence += (w+' ')
                output.write(sentence)
                line = source.readline()
                pbar.update(1)
        print('全部完成，共处理了',str(count),'条')

def help():
    print ("传入参数不足，请使用python fenci.py zhswiki.txt zhswiki_cut.txt 传入待处理的文件和保存的文件名")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        sys.exit(1)
    input, output = sys.argv[1:3]
    cutIt(input,output)
