# 导包 unittest ApiArticle
import unittest

from parameterized import parameterized

from api.api_article import ApiArticle
from tools.read_json import read_json


def get_data_add():
    data = read_json("article_add.json")
    # 新建空列表添加读取数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect"),
                 data.get("status_code")))
    return arrs


def get_data_delete():
    data = read_json("article_del.json")
    # 新建空列表添加读取数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect"),
                 data.get("status_code")))
    return arrs


# 新建测试类
class TestArticle(unittest.TestCase):
    # 新建收藏文章方法
    @parameterized.expand(get_data_add())
    def test_collection(self, url, headers, data, expect, status_code):
        # 临时数据
        # url="http://ttapi.research.itcast.cn/app/v1_0/article/collections"
        # headers={"Content-Type":"application/json","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjIzMDUxMzcsInVzZXJfaWQiOjEzOTg2NDQ1ODU4NjkwODI2MjQsInJlZnJlc2giOmZhbHNlfQ.L5jfzIGyvsM6fb2bIYguD_CP__HrObMInFMLEQUBOHQ"}
        # data={"target":1}
        # 调用收藏文章方法
        r = ApiArticle().api_post_collection(url, headers, data)
        print("收藏响应数据为：", r.json())

        # 断言
        self.assertEqual(status_code, r.status_code)
        self.assertEqual(expect, r.json()['message'])

    # 取消收藏文章方法
    @parameterized.expand(get_data_delete())
    def test_delete_article(self, url, headers, expect, status_code):
        # 临时数据
        # url="http://ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        # headers={"Content-Type":"application/x-www-form-urlencoded","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjIzMDUxMzcsInVzZXJfaWQiOjEzOTg2NDQ1ODU4NjkwODI2MjQsInJlZnJlc2giOmZhbHNlfQ.L5jfzIGyvsM6fb2bIYguD_CP__HrObMInFMLEQUBOHQ"}

        # 调用取消收藏文章方法
        r = ApiArticle().api_delete_article(url, headers)
        print("取消收藏响应数据为：", r.json())
        # 断言
        self.assertEqual(status_code, r.status_code)
        self.assertEqual(expect, r.json()['message'])


if __name__ == '__main__':
    unittest.main()
