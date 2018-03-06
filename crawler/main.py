#!usr/bin/env python
# coding:utf-8

import urllib
import urllib2


url = "https://dtc.ucsf.edu/zh-hans/%e7%b3%96%e5%b0%bf%e7%97%85%e5%88%86%e5%9e%8b/1%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/%e4%ba%86%e8%a7%a31%e5%9e%8b%e7%b3%96%e5%b0%bf%e7%97%85/%e7%b3%96%e5%b0%bf%e7%97%85%e6%a6%82%e5%86%b5/"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
accept_lag = 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
referer = url
headers = {'User-Agent': user_agent, 'Accept-Language': accept_lag, 'Referer': referer}

# geturl = url + "?"+data
# print "get:", geturl

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
print response.read()


enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
