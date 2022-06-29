import jieba

def cutIt(inputFileName,outputFileName):
    output = open(outputFileName,'w',encoding='utf8')
    i = 0
    with open(inputFileName,'r',encoding='utf8') as source:
        line = source.readline()
        count = 0
        while line:
            sentence = ''
            count += 1
            for w in jieba.cut(line):
                sentence += (w+' ')
            output.write(sentence)
            if count == 10000:
                i += 1
                print('已完成',str(i),'条')
                count = 0
            line = source.readline()
        print('全部完成，共处理了',str(count),'条')

cutIt('zhswiki.txt','zhswiki_cut.txt')