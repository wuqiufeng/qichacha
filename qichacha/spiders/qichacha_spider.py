# -*- coding: utf-8 -*-

import scrapy
from qichacha.items import QichachaItem


# 创建一个爬虫类
class QichachaSpider(scrapy.Spider):
    # 爬虫名
    name = "qichacha"
    # 允许爬虫作用的范围
    # allowed_domains = ["qichacha.com"]
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫起始的url
    # start_urls = [
    #     "http://www.qichacha.com/search?key=%E5%89%8D%E6%B5%B7%E4%BC%81%E4%BF%9D%E7%A7%91%E6%8A%80",
    # ]

    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#aandroid"
    ]

    def parse(self, response):
        with open("qichichi.html", "w") as f:
            f.write(response.body.decode('utf8'))

    # def parse_item(self, response):
    #     pass

    # """
    # GET http://www.qichacha.com/search?key=%E5%89%8D%E6%B5%B7%E4%BC%81%E4%BF%9D%E7%A7%91%E6%8A%80 HTTP/1.1
    # Host: www.qichacha.com
    # Connection: keep-alive
    # Upgrade-Insecure-Requests: 1
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    # Referer: http://www.qichacha.com/search?key=%E5%89%8D%E6%B5%B7%E4%BC%81%E4%BF%9D%E7%A7%91%E6%8A%80
    # Accept-Encoding: gzip, deflate
    # Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    # Cookie: UM_distinctid=162196857a4593-01178dbbc2f2b-7b113d-1fa400-162196857a5707; _uab_collina=152084469931485327671868; _umdata=E2AE90FA4E0E42DEF4ACDDBC8924F21B2A1D6C3F69441D89250A95381DC1234C92709F2B0ED9DBDECD43AD3E795C914C6272F203BEFB77ED4C942F2F9B57BC89; PHPSESSID=2mt2vinp7vc4m2v1thc7gdjca7; hasShow=1; acw_tc=AQAAAL5iClWSCAQAWipzG+BhlziskQvx; zg_did=%7B%22did%22%3A%20%22162196858f8cac-0bda5ce8763936-7b113d-1fa400-162196858f9a6a%22%7D; CNZZDATA1254842228=180668192-1520840155-https%253A%252F%252Fwww.baidu.com%252F%7C1520917522; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1520847780,1520848320,1520914411,1520914445; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1520919126; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201520918862159%2C%22updated%22%3A%201520919146412%2C%22info%22%3A%201520844691710%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22097f12626e89efe9b8bdbc498efbbd02%22%7D
    #
    # //a[@onclick="zhugeTrack('企业搜索-列表-公司名称')"]
    # //*[@id="searchlist"]//a[@class="ma_h1"]//@href
    # """
