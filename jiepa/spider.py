import json
import os
import re
from multiprocessing.pool import Pool
import requests
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urlencode
from hashlib import md5
from bs4 import BeautifulSoup
from config import *

# 声明MongoDB对象
client = pymongo.MongoClient(MONGO_URL, 27017)
db = client[MONGO_DB]


# 获取索引页
def get_index_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # 解析json格式返回字典格式
    except requests.exceptions.ConnectionError:
        print("Request index page failed!")
        return None


# 解析索引页
def parse_index_page(json):
    if json.get('data'):
        for item in json.get('data'):
            abstract = item.get('abstract')
            article_url = item.get('article_url')
            yield {
                'abstract': abstract,
                'article_url': article_url,
            }


# 获取详情页
def get_detail_page(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.ConnectionError:
        print('Request detail page failed!')
        return None


# 解析综合详情页
def parse_detail_page(html):
    doc = pq(html)
    title = re.sub(r'[\\/:*?"<>→]', '', doc('title').text())
    # 利用正则提取图片地址
    pattern = re.compile('&quot;(http.*?)&quot;', re.S)
    results = re.findall(pattern, html)
    if results:
        yield {
            'title': title,
            'images_url': results
        }


def parse_detail_gallary(html):
    # 获取详情页的标题和图片地址
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    title = re.sub(r'[\s*\\/:\*\?\|<>→]', '', title)
    # 正则提取图集中个图片地址
    pattern = re.compile('.*?gallery: JSON.parse\("(.*?)\"\)', re.S)
    result = re.search(pattern, html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            # 提取图片
            images = [item.get('url') for item in sub_images]
            if images:
                yield {
                    'title': title,
                    'images_url': images
                }


def save_images(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    for img_url in item['images_url']:
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                        print("Save successfully")
                else:
                    print('Already Downloaded', file_path)
        except requests.exceptions.ConnectionError:
            print("Failed To Save Image!")


# save to mongodb
def save_mongo(item):
    if db[MONGO_TABLE].insert(item):
        print('successfully saved to mongodb!')


def main(offset):
    json = get_index_page(offset)
    for item in parse_index_page(json):
        article_url = item['article_url']
        if article_url and item['abstract'] and None:
            html = get_detail_page(article_url)
            for it in parse_detail_page(html):
                save_images(it)
        elif article_url and not item['abstract']:
            html = get_detail_page(article_url)
            for it in parse_detail_gallary(html):
                save_images(it)


if __name__ == '__main__':
    pool = Pool(3)
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
