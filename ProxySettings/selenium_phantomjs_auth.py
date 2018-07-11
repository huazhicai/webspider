from selenium import webdriver


service_args = [
    '--proxy=',
    '--proxy-type=http',
    '--proxy-auth=username:password'
]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)