#coding=utf-8
import requests
import re
from lxml import etree

print("http://www.xiazai520.xyz/")
print("数据在:"+"http://www.xiazai520.xyz/movie")

def get_cate_info(url):#创建函数
    res = requests.get(url)
    res.encoding = 'gb2312'#enconding表示的是页面接受的数据编码类型
    html = etree.HTML(res.text)
    infos = html.xpath('//div[@class="contain"]/ul/li[position()<12]')
    for info in infos:
        cate_name = info.xpath('a/text()')[0]
        cate_url = res.url + info.xpath('a/@href')[0]
        get_movie(cate_url,cate_name)

def get_movie(url,cate_name):
    res = requests.get(url)
    res.encoding = 'gb2312'
    all_page = re.findall('共(.*?)页', res.text)#计算共需要爬取多少页
    kind = re.findall('<option value=\'(list_.*?_).*?', res.text)#这句没看懂
    if len(all_page) > 0:
        kind_url = url.rstrip(url.split('/')[-1]) + str(kind[0])
        for page in range(1,int(all_page[0])+1):
            page_url = kind_url + str(page) + '.html'
            resp = requests.get(page_url)
            resp.encoding = 'gb2312'
            html = etree.HTML(resp.text)
            infos = html.xpath('//div[@class="co_content8"]/ul//table')
            for info in infos:
                detail_url = 'http://www.ygdy8.com' + info.xpath('tr[2]/td[2]/b/a/@href')[0]
                movie_name = info.xpath('tr[2]/td[2]/b/a/text()')[0]
                print(detail_url)
                get_resource(detail_url, cate_name, url, movie_name)

def get_resource(url,cate_name,cate_url,movie_name):
    res = requests.get(url)
    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    movie_resource = html.xpath('//tbody//tr/td/a/text()')[0]
    print(movie_resource)

if __name__ == '__main__':
    urls = ['http://www.ygdy8.com'.format(str(i)) for i in range(1,94)]
    for url in urls:
        get_cate_info(url)

