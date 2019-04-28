### 登录github,查看资料信息

- **分析过程**
    - 登录是，数据通过表单传输，方法是post, 在浏览器中抓取登录过程的request_url:https://github.com/session
    - 查看表单数据，发现authenticity_token， 需要在登录页面提取
    - 因为登录后要有操作，所以需要使用requests.session()

- **遇到的问题**
    - etree返回的都是列表