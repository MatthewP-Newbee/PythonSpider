#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: PythonSpider
# @Date: 2019/1/2
# @Author: MatthewP

from lxml import etree
import requests
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
                image_url = elem.get_attribute('href')
                self.download_image(image_url)

    def download_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            image = html.xpath('//main/section/div/img/@src')[0]
            id = html.xpath('//main/section/div/img/@data-wallpaper-id')[0]
            image_path = ''.join(['https:', image])
            image_response = requests.get(image_path)
            if image_response.status_code == 200:
                contents = image_response.content
                with open(f'../../Downloads/AnimalImages/{id}.jpg', 'wb') as fh:
                    fh.write(contents)

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
    AnmWallpapers(3)