import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def get_token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token()[0],
            'login': email,
            'password': password,
            'webauthn-support': 'supported'
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//li[@class="public source no-description"]')
        for item in dynamics:
            dynamic = ', '.join(item.xpath('//span[@class="css-truncate css-truncate-target"]//text()'))
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//*[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//*[@id="user_profile_email"]/option[2]/@value')
        print(name, email)


if __name__ == '__main__':
    login = Login()
    login.login(email='936844218@qq.com', password='110huazhicai')

