import requests
from lxml import etree
import pymysql
import datetime
import unicodedata
import re
import string
import random
import time

class zhidao(object):
    def __init__(self):
        self.noise_tokens = [ "2113", "5261", "4102", "1653"]
        self.cnx = pymysql.connect(user='root', password='1995811a',
                    host='localhost', database='aerospace')
        self.cursor = self.cnx.cursor()
    
    def has_crawl(self, url):
        select_stmt = "SELECT 1 FROM zhidao WHERE `url` = %s"
        self.cursor.execute(select_stmt, (url,))
        qresult = self.cursor.fetchone()
        return qresult
            
    def get_urlkeys(self):
        select_stmt = "SELECT `url`, `key` FROM zhidao_q WHERE `has_crawl` = 0"
        self.cursor.execute(select_stmt)
        urlkeys = self.cursor.fetchall()
        print('还剩下{}条数据'.format(len(urlkeys)))
        return urlkeys
    
    def insert_data(self, result):
            print('开始插入{}-{}'.format(result['title'], result['url']))
            insert_stmt = "INSERT INTO zhidao (`url`, `key`, `title`,  `best_answer`, `other_answers`, `create_date`) VALUES (%s, %s, %s,%s, %s, %s)"
            data = (result['url'], result['key'], result['title'], result['best_answer'], result['other_answers'], datetime.datetime.now())
            self.cursor.execute(insert_stmt, data)  

    def update_zhidaoq(self, result):
        print('更新状态-URL{}'.format(result['url']))
        try:
            update_stmt = "UPDATE zhidao_q SET `has_crawl`=1 WHERE `url`= %s"
            self.cursor.execute(update_stmt, (result['url'],))
        except:
            print('zhihu_q未找到-URL{}，重新插入...'.format(result['url']))
            insert_stmt = "INSERT INTO zhidao_q (`url`, `key`, `title`,  `answer`, `has_crawl`, `create_date`) VALUES (%s, %s, %s,%s, %s, %s)"
            data = (result['url'], result['key'], result['title'], result['best_answer'],  1, datetime.datetime.now())
            self.cursor.execute(insert_stmt, data) 

    def crawl_zhidao(self):
        urlkeys = self.get_urlkeys()
        for url, key in urlkeys:
            if self.has_crawl(url):
                print('{}-已经爬过',format(url))
                continue 
            print('开始{}'.format(url))

            response = requests.get(url)
            html = etree.HTML(response.text)
            title = html.xpath('//*[@id="wgt-ask"]/h1/span//text()')
            print(title)
            print('==============================')
            best_answer = html.xpath('//div[@class="best-text mb-10 dd"]//text()')
            print(best_answer)
            print('==============================')
            other_answers = html.xpath('//div[@class="answer-text mb-10"]//text()')    
            print(other_answers)
            print('==============================')

            if best_answer or other_answers:
                item = {'title': self.normalize(''.join(title).strip()), 'best_answer': self.normalize(''.join(best_answer).strip()), \
                        "other_answers": self.normalize(''.join(other_answers).strip()), "url": url, 'key':self.normalize(key.strip())}
                try:
                    self.insert_data(item)
                    self.update_zhidaoq(item)
                    self.cnx.commit()
                    print('插入&更新状态成功！')
                except:
                    print('插入zhudao报错！')

                time.sleep(random.randint(1, 10))

        self.cursor.close()
        self.cnx.close()  
                        
    def normalize(self, answer):
        unicodedata.normalize('NFKC', answer)
        answer = re.sub("\n展开全部\n", "", answer)
        answer = re.sub("\\n+", "", answer)
        answer = re.sub("\u3000", "", answer)
        not_chinese_lst = re.findall("[A-Za-z0-9]+", answer)
        for w in not_chinese_lst:
            if 40 <= len(w) <= 58:
                answer = answer.replace(w, "")
            if len(w) > 58:
                answer = answer.replace(w[:58], "")
        for noisy_token in self.noise_tokens:
            answer = re.sub(noisy_token, "", answer)

        for noisy_data in ["bai", "du", "zhi", "dao", "copy"]:
            tmp_lst = re.findall(noisy_data + ".", answer)
            for tmp in tmp_lst:
                if len(tmp) == len(noisy_data) or not tmp[-1] in string.ascii_letters:
                    answer = answer.replace(noisy_data, "")
        answer = answer.replace("\xa0", "")
        return answer
    
if __name__ == '__main__':
    spider = zhidao()
    spider.crawl_zhidao()