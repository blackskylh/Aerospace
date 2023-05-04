import pymysql
import datetime
from baiduspider import BaiduSpider

spider = BaiduSpider()
cnx = pymysql.connect(user='root', password='1995811a',
                              host='localhost', database='aerospace')

# 创建游标对象
cursor = cnx.cursor()
page_size = 3
keywords = ['航空航天知识', 'aerospace']

def has_crawl(url):
    select_stmt = "SELECT 1 FROM zhidao_q WHERE `url` = %s"
    cursor.execute(select_stmt, (url,))
    qresult = cursor.fetchone()
    return qresult

def insert_data(result):
        print('开始插入{}-{}'.format(result['title'], result['url']))
        insert_stmt = "INSERT INTO zhidao_q (`url`, `key`, `title`, `question`, `answer`, `date`, `count`, `agree`, `answerer`, `create_date`,`has_crawl`) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s)"
        data = (result['url'], key, result['title'], result['question'], result['answer'], result['date'], result['count'], result['agree'], result['answerer'], datetime.datetime.now(), 0)
        cursor.execute(insert_stmt, data)    

for key in keywords:
    for page in range(1, page_size+1):
        print("开始爬取页面{}".format(page))
        reslst = spider.search_zhidao(key, pn=page).plain
        if not len(reslst): continue
        for result in reslst:
            print(result)
            # 执行查询语句，检查数据是否已经存在
            if has_crawl(result['url']):
                print("数据已存在！")
                continue
            # 插入表格
            insert_data(result=result)
            # 提交事务
            cnx.commit()

# 关闭游标和数据库连接
cursor.close()
cnx.close()