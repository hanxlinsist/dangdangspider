# dangdangspider
爬取当当网上最受欢迎的计算机书籍

## 配置信息

1. 在命令行上定义一个日志文件，它将代替终端上的日志输出.
scrapy crawl dangdang -s LOG_FILE=dd.log  


2. 把爬取的信息以不同的文件格式保存
    - scrapy crawl article -o articles.csv -t csv
    - scrapy crawl article -o articles.json -t json
    - scrapy crawl article -o articles.xml -t xml







