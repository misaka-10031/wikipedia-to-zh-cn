# 将维基百科打包转换为语料库

## 使用方式

下载-导出-简繁体转换-分词（可选）  
需要安装的依赖：  
> pip install gensim,jieba  

### 下载

直接从此地址下载后存放在本目录即可  
<https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2>  
（可能需要科学上网）

## 使用脚本完成（仅限中文维基）

> 请确认你已经完整clone了本项目<https://github.com/misaka-10031/wikipedia-to-zh-cn>  
> 按照规范将下载的Wiki原始数据包移动到此git目录中  
> 完成OpenCC软件的下载与环境变量PATH设置(详见下文“简繁体转换”章节)  
> 并确保你的磁盘有足够的剩余空间（大约是xml.bz2文件的2-3倍大小）来存储中间过程和结果  

```bash
bash.bat
```

## 手动完成

### 导出

使用维基百科提供的工具 gensim，开始导出  

> python process_wiki.py zhwiki-latest-pages-articles.xml.bz2 zhwikiraw.txt  

### 简繁体转换

下载并解压[OpenCC](https://github.com/BYVoid/OpenCC)到任意位置  
将 'OpenCC/build/bin' 添加到环境变量PATH  
cmd执行指令：  
> opencc -i zhwikiraw.txt -o zhswiki.txt -c t2s.json  

### 分词

(请确保上一步输出文件名为zhswiki.txt)  
> fenci.py zhswiki.txt zhswiki_cut.txt  
输出的zhswiki_cut.txt，就是最终结果啦  

## 感谢

[chenbjin](https://github.com/chenbjin) process_wiki.py的原始撰写者，优秀的机器学习工程师  
Wikipedia 维基百科  
[OpenCC](https://github.com/BYVoid/OpenCC) 一款开源的简繁体转换工具  

## TODO

接下来可能写一个Win下自动下载注册OpenCC的脚本？  
下次一定  
