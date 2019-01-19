## scrapy selenium taobao

- **对接selenium**
    - 其实就是在downloaderMiddleware 处理request，
    - 返回一个HtmlResponse对象，
    - process_request(request, spider)后续的process_request和process_exception
    - 就不调用了，调用更低级的process_response处理，然后直接给到spider