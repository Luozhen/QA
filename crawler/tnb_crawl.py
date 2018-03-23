#!usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import traceback
from bs4 import BeautifulSoup

class Info(object):
    def __init__(self, url):
        self.url = url
        self.headers = self.__init_header()

    def __init_header(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'
        accept_lag = 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
        headers = {'User-Agent': user_agent, 'Accept-Language': accept_lag}
        return headers


class Unit_Crawler(Info):
    def __init__(self, url):
        super(Unit_Crawler, self).__init__(url)

    def handle_html(self, html):
        title = None
        text = None
        url_ls = []
        try:
            soup = BeautifulSoup(html, "html5lib")
            find_title = soup.find('h1', attrs={'class': 'entry-title'})
            if find_title:
                title = unicode(find_title.string)
            soup_content = soup.find_all('div', attrs={'id': 'primary-content'})[0]
            text = soup_content.get_text().strip().replace('\n', ' ')
            href_ls = soup_content.find_all('a')
            for href_tag in href_ls:
                url_ls.append(href_tag.get('href'))
        except Exception as e:
            traceback.print_exc()
            print e.message, "\n"
        return title, text, url_ls

    def crawler(self):
        title = None
        text = None
        url_ls = None
        try:
            request = urllib2.Request(self.url, headers=self.headers)
            response = urllib2.urlopen(request)
            html = response.read()
            title, text, url_ls = self.handle_html(html)
        except Exception as e:
            traceback.print_exc()
            print e, "\n"
        return title, text, url_ls


class Main_Crawler(object):
    def __init__(self, url, filename):
        self.file_name = filename
        self.urls = []
        self.urls_set = set([])

        self.__init_urls(url)

    def __init_urls(self, url):
        self.cur_idx = 0
        self.urls.append(url)
        self.urls_set.add(url)

    def write_text(self, title, text):
        if not text or not title:
            return
        with open(self.file_name, 'a') as src:
            content = title + u' ' + text + u'\n'
            src.write(content.encode('utf-8'))

    def update_urls(self, url_ls):
        if not url_ls:
            return
        for url in url_ls:
            if url not in self.urls_set:
                self.urls.append(url)
                self.urls_set.add(url)

    def run(self):
        while self.cur_idx < len(self.urls):
            print "\ncurrent_idx:", self.cur_idx, "of", len(self.urls)
            cur_url = self.urls[self.cur_idx]
            unit_crawler = Unit_Crawler(cur_url)
            title, text, url_ls = unit_crawler.crawler()

            self.cur_idx += 1
            self.write_text(title, text)
            self.update_urls(url_ls)


if __name__ == "__main__":
    url = "https://dtc.ucsf.edu/zh-hans/%E7%B3%96%E5%B0%BF%E7%97%85%E5%88%86%E5%9E%8B/"
    file_name = "data/tnb_1.txt"
    crawler = Main_Crawler(url, file_name)
    crawler.run()