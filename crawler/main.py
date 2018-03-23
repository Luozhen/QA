#!usr/bin/env python
# coding:utf-8

import urllib
import urllib2
from bs4 import BeautifulSoup



url = "https://dtc.ucsf.edu/zh-hans/%E7%B3%96%E5%B0%BF%E7%97%85%E5%88%86%E5%9E%8B/"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'
accept_lag = 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
referer = url
headers = {'User-Agent': user_agent, 'Accept-Language': accept_lag} #, 'Referer': referer}

# geturl = url + "?"+data
# print "get:", geturl

# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request)
# html = response.read()
# for string in soup.stripped_strings():
#     print string, repr(string)
html = '''<div id="content" class="hfeed"><div class="post-2170 page type-page status-publish hentry entry"><h1 class="entry-title">糖尿病分型</h1>

<ul class="marthaNav">
<li class="marthaNext first">
<a href="https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/1%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/" title="1型糖尿病">1型糖尿病</a> »</li><li class="marthaPrev last">« 
<a href="https://dtc.ucsf.edu/zh-hans/" title="主页">主页</a>
</li>
</ul>

<div id="custom-page-content"><p class="img-container"><img class="alignnone size-full wp-image-1859" alt="diabetes definition" src="/wp-content/uploads/2010/09/dtc_000006850190.jpg" width="226" height="150"></p>
<h2>很多因素会导致血糖升高</h2>
<p>糖尿病按病因分型，了解您患有哪类糖尿病，有助于糖尿病的控制。</p>
</div><div class="sidebar-image-holder"><a class="gift-image" target="_blank" href="https://makeagift.ucsf.edu/dtc"><img class="wp-image-6931 size-full aligncenter" src="https://dtc.ucsf.edu/wp-content/uploads/2010/08/Untitled-4.png" width="128" height="105"></a></div> 

 <div class="entry-content"><div id="primary-content">
<div id="page-highlight">糖尿病的定义是血糖升高。血糖升高的原因有很多。按照不同的病因，糖尿病可分为不同的类型。根据导致糖尿病的不同病因，治疗也会有所不同。重要的是了解您患有什么类型的糖尿病，因为您这一型糖尿病的治疗方法，可能与别人的糖尿病不同。本节将帮助您了解您患有什么类型的糖尿病。</div>
<h2>在这一节里，你会了解：</h2>
<ul class="bigBullets">
<li class="first"><a href="https://dtc.ucsf.edu/zh-hans/%E7%B3%96%E5%B0%BF%E7%97%85%E5%88%86%E5%9E%8B/1%E5%9E%8B%E7%B3%96%E5%B0%BF%E7%97%85/%E4%BA%86%E8%A7%A3%E7%B3%96%E5%B0%BF%E7%97%85/1%E5%9E%8B%E7%B3%96%E5%B0%BF%E7%97%85%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98/">1型糖尿病</a>：<br>
指身体完全丧失了制造胰岛素的能力，或只能制造极少量的胰岛素。1型糖尿病通常由自身免疫引起，就是说身体的免疫系统错误地破坏了分泌胰岛素的细胞。大约10%糖尿病人属于1型糖尿病。</li>
<li><a href="https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/2%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/%e4%ba%86%e8%a7%a32%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/2%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85%e5%b8%b8%e8%a7%81%e9%97%ae%e9%a2%98%e8%a7%a3%e7%ad%94/">2型糖尿病</a>：<br>
由两方面因素造成：胰岛素抵抗，以及身体不能制造足够的胰岛素来克服胰岛素抵抗。2型糖尿病是最常见的糖尿病类型，占全世界糖尿病患者的80%–90%。</li>
<li><a href="https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/%e5%85%b6%e5%ae%83%e7%b1%bb%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/">其他类型糖尿病</a>：<br>
包括不寻常的或罕见的遗传性或获得性糖尿病，只有少数糖尿病人属于此种情况。</li>
<li><a href="https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/%e5%a6%8a%e5%a8%a0%e7%b3%96%e5%b0%bf%e7%97%85/">妊娠糖尿病</a>：<br>
在妊娠期间诊断的糖尿病。</li>
<li class="last"><a href="https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b%e8%a1%a8/">糖尿病分型表</a>：<br>
可快速查找糖尿病成因。</li>
</ul>
</div>
</div>
<ul class="marthaNav">
<li class="marthaNext first">
<a href="https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/1%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/" title="1型糖尿病">1型糖尿病</a> »</li><li class="marthaPrev last">« 
<a href="https://dtc.ucsf.edu/zh-hans/" title="主页">主页</a>
</li>
</ul>

 </div></div>'''
soup = BeautifulSoup(html, "html5lib")
# print soup
title = soup.find('h1', attrs={'class': 'entry-title'}).string
soup_content = soup.find_all('div', attrs={'id': 'primary-content'})[0]

href_ls = soup_content.find_all('all')
text = soup_content.get_text().strip().replace('\n', ' ')
print text, "\n-----"
uni_title = unicode(title)
print title, uni_title, type(uni_title), "\n\n"
for href_tag in href_ls:
    href = href_tag.get('href')
    print href, type(href), "\n"


# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
