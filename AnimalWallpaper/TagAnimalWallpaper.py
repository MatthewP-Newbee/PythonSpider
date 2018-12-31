#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: PythonSpider
# @Date: 2018/12/31
# @Author: MatthewP

import requests
import string
import random
from lxml import etree
from urllib.parse import urlencode


class Animal(object):
    def __init__(self, page_num):
        self.num = page_num
        self.run()

    def run(self):
        for i in range(1, self.num + 1):
            url = self.get_url(i)
            text = self.get_request(url)
            self.get_image(text)

    def get_url(self, page):
        params = {
            'q': 'id:82',
            'page': page
        }
        base_url = 'https://alpha.wallhaven.cc/search?'
        url = base_url + urlencode(params)
        return url

    def get_request(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            text = response.text
            return text
        else:
            print(f'Fail getting {url}')
            return None

    def get_image(self, text):
        tree = etree.HTML(text)
        figs = tree.xpath('//ul/li/figure')
        for fig in figs:
            name = fig.get('data-wallpaper-id') or self.rd_str()
            imgs = fig.xpath('./img')
            for img in imgs:
                try:
                    path = img.xpath('./@data-src')
                    response = requests.get(path[0])
                    if response.status_code == 200:
                        content = response.content
                        with open(f'../../Downloads/Animals/{name}.jpg', 'wb') as fh:
                            fh.write(content)
                except requests.ConnectionError as e:
                    print(e)

    def rd_str(self):
        chars = string.ascii_letters + string.digits
        random_str = ''.join([random.choice(chars) for x in range(9)])
        return random_str

if __name__ == '__main__':
    Animal(10)


