# coding:utf-8
import requests
from bs4 import BeautifulSoup as bs

print("http://www.xiazai520.xyz/")
print("数据在:"+"http://www.xiazai520.xyz/movie")

# 爬取入口
rooturl = "http://www.ygdy8.com/index.html"
# 获取网页源码
res = requests.get(rooturl)
# 网站编码gb2312
res.encoding = 'gb2312'
# 网页源码
html = res.text
soup = bs(html, 'html.parser')
cate_urls = []
for cateurl in soup.select('.contain ul li a'):
    # 网站分类标题
    cate_name = cateurl.text.encode('utf-8')
    # 分类url 进行再次爬取
    cate_url = "http://www.ygdy8.com/" + cateurl['href']
    cate_urls.append(cate_url)
    print "网站一级菜单:", cate_name, "菜单网址：", cate_url
    # newdir = "E:/moive24/"+ cate_name
    # os.makedirs(newdir.decode("utf-8"))
    # print "创建分类目录成功------" + newdir
# 每个菜单url 解析
for i in range(len(cate_urls)):
    cate_listurl = cate_urls[i]
    res = requests.get(cate_listurl)
    res.encoding = 'gb2312'
    html = res.text
    soup = bs(html, 'html.parser')
    print "正在解析第" + str(i + 1) + "个链接", cate_urls[i]
    contenturls = []
    contents = soup.select('.co_content8 ul')[0].select('a')
    # print contents
    for title in contents:
        moivetitle = title.text.encode('utf-8')
        moiveurl = "http://www.ygdy8.com/" + title['href']
        contenturls.append(moiveurl)
        #print moivetitle, moiveurl
        # file_name=newdir +'/'+ moivetitle +'.txt'
        # print file_name
        # f = open(file_name.decode("utf-8"), "wb")
        # f.close()
        res = requests.get(moiveurl)
        res.encoding = 'gb2312'
        html = res.text
        soup = bs(html, 'html.parser')
        moive_sources = soup.select('#Zoom span tbody tr td a')
        for source in moive_sources:
            moive_source = source['href']
            print moive_source
            f = open('E:\python web\movie web/moive.txt', 'a')
            f.write(moive_source.encode("utf-8") + "\n")
            f.close()