from selenium import webdriver

proxy = '122.114.31.177:808'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+ proxy)
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://httpbin.org/get')
