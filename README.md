# 冬奥会项目

##### windows系统

#### 创建数据库环境

1. 确保windows系统下安装MySQL（版本号mysql-8.0.33-winx64）
2. 创建数据库aerospace，并在其中创建两个表**zhihu**和**zhihu_q**(具体的SQL详见**zhihu.sql**和**zhihu_q.sql**)
3. 修改数据库登录配置1）Baidu_spider/search_zhidao.py第6-7行；2）baiduzhidao/spiders/baiduzhidao.py第19-20行

#### 根据关键词爬取百度知道的URL

1. pip install -r requirements --安装所需python包
2. 修改关键词列表（关键词列表详见Baidu_spider/search_zhidao.py的第**12**行）
3. python Baidu_spider/search_zhidao.py --根据关键词从百度搜索引擎中爬取**百度知道**的URL、主题等存入**zhihu_q**数据表

#### 根据爬取的百度知道URL爬取相关的回答

1. scrapy crawl baidu_zhidao --根据百度知道的**URL**爬取相关答案存入**zhihu_q**数据表

