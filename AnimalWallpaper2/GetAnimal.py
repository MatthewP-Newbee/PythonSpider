#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: PythonSpider
# @Date: 2019/1/2
# @Author: MatthewP

import requests
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
                elem.click()
                image_handle = driver.window_handles[1]
                driver.switch_to.window(image_handle)
                wait = WebDriverWait(driver, 100)
                wait.until(EC.presence_of_element_located((By.XPATH, '//main/section/div/img')))
                image_elem = driver.find_element(By.XPATH, '//main/section/div/img')
                image_id = image_elem.get_attribute('data-wallpaper-id')
                image_url = image_elem.get_attribute('src')
                self.download_image(image_url, image_id)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

    def download_image(self, url, id):
        print(url)
        image_response = requests.get(url)
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