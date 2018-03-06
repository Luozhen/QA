#!usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import re

page = 1
url = 'https://www.qiushibaike.com/hot/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
    content = response.read().decode('utf-8')
    pattern = re.compile(
        '<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',
        re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0], item[1], item[2], item[3], item[4]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

