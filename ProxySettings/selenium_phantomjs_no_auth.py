from selenium import webdriver

service_args = [
    '--proxy=118.190.95.43:9001'
    '--proxy-type=http'
]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)