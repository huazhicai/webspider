import os

from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from config import *
from pyquery import PyQuery as pq
import pymongo

profile_dir = r'C:\Users\admin\AppData\Local\Google\Chrome\User Data'
chrome_options = Options()
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('disable-web-security')
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
# chrome_options.add_argument('--headless')

browser = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(browser, 10)

client = pymongo.MongoClient(MONGO_URL)
db = client['MONGO_DB']


def index_page(page):
    print('Crawling {} page'.format(page))
    try:
        url = 'https://s.taobao.com/search?q=ipad'
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    resolve products data
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        products = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(products)
        save_to_mongo(products)


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('Successfully saved to MongoDB!')
    except Exception:
        print('saved to MongoDB failed!')


def main():
    """
    Traversing each page
    :return:
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    main()
