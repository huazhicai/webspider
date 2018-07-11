import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import CLientError
except:
    from aiohttp import ClientConnectionError as ProxyConnetionError
from proxypool.db import RedisClient
from proxypool.setting import *


class Tester(object):

    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self, proxy):
        """
        测试单个代理
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print("正在测试", proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print("代理可用", proxy)
                    else:
                        self.redis.decrease(proxy)
            except (
            aiohttp.ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败', proxy)

    def run(self):
        print("测试器开始运行")
        try:
            count = self.redis.count()
            print()
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i+BATCH_TEST_SIZE, count)
                print()