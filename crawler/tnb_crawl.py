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

        soup = BeautifulSoup(html, "html5lib")
        primary_content = soup.find_all('div', attrs={'id': 'primary-content'})
        content = soup.find_all('div', attrs={'id': 'content'})
        if primary_content or content:
            content = primary_content[0] if primary_content else content[0]
            text = content.get_text().strip().replace('\n', ' ')
            href_ls = content.find_all('a')
            for href_tag in href_ls:
                url_ls.append(href_tag.get('href'))
        find_title = soup.find('h1', attrs={'class': 'entry-title'})
        if find_title:
            title = unicode(find_title.string)

        return title, text, url_ls

    def crawler(self):

        request = urllib2.Request(self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        html = response.read()
        title, text, url_ls = self.handle_html(html)

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
            content = title + u'\t' + text + u'\n'
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
            url_ls = None
            try:
                title, text, url_ls = unit_crawler.crawler()

                self.write_text(title, text)

            except Exception as e:
                traceback.print_exc()
            finally:
                if url_ls:
                    self.update_urls(url_ls)
                self.cur_idx += 1


if __name__ == "__main__":
    url = "https://dtc.ucsf.edu/zh-hans/%E7%B3%96%E5%B0%BF%E7%97%85%E5%88%86%E5%9E%8B/1%E5%9E%8B%E7%B3%96%E5%B0%BF%E7%97%85/1%E5%9E%8B%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84%E6%B2%BB%E7%96%97/%E8%8D%AF%E7%89%A9%E5%8F%8A%E6%B2%BB%E7%96%97/1%E5%9E%8B%E7%B3%96%E5%B0%BF%E7%97%85-%E8%83%B0%E5%B2%9B%E7%B4%A0%E6%B2%BB%E7%96%97/"
    file_name = "data/tnb_2.txt"
    crawler = Main_Crawler(url, file_name)
    crawler.run()
