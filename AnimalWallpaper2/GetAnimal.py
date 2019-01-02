#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: PythonSpider
# @Date: 2019/1/2
# @Author: MatthewP

from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnmWallpapers(object):
    def __init__(self, page_unm):
        self._num = page_unm
        self.run()

    def run(self):
        for i in range(1, self._num + 1):
            url = self.get_url(i)
            driver = self.one_page(url)

            elems = driver.find_elements(By.XPATH, '//ul/li/figure/a')
            for elem in elems:
                print(elem)
                elem.click()
                print(elem)
                print('******************')

    def one_page(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        return driver

    def get_url(self, page):
        params = {
            'q': 'id:82',
            'page': page
        }
        base_url = 'https://alpha.wallhaven.cc/search?'
        url = base_url + urlencode(params)
        return url

if __name__ == '__main__':
    AnmWallpapers(1)