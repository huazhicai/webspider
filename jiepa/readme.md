### Ajax 分析爬取今日头条街拍美图

- **准备工作**
    - python3.6
    - MongoDB 
    - requets
    - pymongo
    
- **分析过程**
    - 逆向思维：需求分析，需要爬取图片，那么就需要找到图片链接地址
      搜索框搜索 "街拍" , 打开开发者选项:Network:XHR
      下拉进度条，Ajax异步加载数据，点击Preview查看分析数据
      ![1](1.png)
      url_list 里的url不全，而且图片不是高清大图，因此，需要到详图里面去提取图片的url
      详图有两种情况：一种是所有图片在一个面页面内的单面式；另一种是图集式。两种排版的response body格式不一样
      因此，要分别提取
      ![单面排版](2.png)
      
      ![图集排版](3.png)
    
    - 可以通过abstract来区分,abstract为空的就是图集排版， 然后利用正则表达式提取图片的url
    
- **保存文件**
    - 二进制文件写入，为防止重复，使用md5命名
    
- **遇到的问题**
    - ajax里的数据，图片的url不全，且是模糊的小图，因此需要详情页提取url，两种详情页
    返回的response body格式不一，需要分别用正则提取
    
    - 图片量大，而且重爬会重复，因此，考虑用md5加密的命名方式来命名
    
[源码链接](https://github.com/huazhicai/Python3WebSpider/tree/master/jiepai)