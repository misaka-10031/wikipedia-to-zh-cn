echo off
echo 欢迎使用维基分词一键脚本
echo 请确认你已经完整clone了https://github.com/misaka-10031/wikipedia-to-zh-cn
echo 安装了python3.8+版本并添加到了PATH环境变量中
echo 使用pip install安装了gensim与jieba
echo 按照规范将下载的Wiki原始数据包移动到此脚本所在目录
echo 完成OpenCC软件的下载与PATH环境变量配置
echo 并确保你的磁盘有足够的剩余空间（大约是xml.bz2文件的2-3倍大小）来存储中间过程和结果
set /p sure=确认请按回车，取消请按Ctrl+C
echo 开始从Wiki原始数据包中提取中文词条
python process_wiki.py zhwiki-latest-pages-articles.xml.bz2 zhwikiraw.txt
echo 开始OpenCC转换
opencc -i zhwikiraw.txt -o zhswiki.txt -c t2s.json
echo 开始分词
python fenci.py zhswiki.txt zhswiki_cut.txt
echo 全部完成，输出文件在zhswiki_cut.txt