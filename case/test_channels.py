#导包 unittest ApiChannels
import unittest

from parameterized import parameterized

from api.api_channels import ApiChannels
from tools.read_json_more import read_json


def get_data():
    data = read_json("channels.json")


#新建测试类
class TestChannels(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,expect,status_code):
        s = ApiChannels().api_channels(url,headers)
        print("响应结果：",s.json())
        self.assertEqual(expect,s.json()['message'])
        self.assertEqual(status_code,s.status_code)
