#导包 unittest ApiChannels
import unittest

from parameterized import parameterized

from api.api_channels import ApiChannels
from tools.read_json import read_json


def get_data():
    datas = read_json("channels.json")
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("headers"),
                     data.get("expect"),
                     data.get("status_code")))
    return arrs

#新建测试类
class TestChannels(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data())
    def test_channels(self, url, headers, expect, status_code):
        # #临时数据
        # url="http://ttapi.research.itcast.cn/app/v1_0/user/channels"
        # #token之前有个空格和Bearer
        # headers={"Content-Type":"application/json","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjIzMDUxMzcsInVzZXJfaWQiOjEzOTg2NDQ1ODU4NjkwODI2MjQsInJlZnJlc2giOmZhbHNlfQ.L5jfzIGyvsM6fb2bIYguD_CP__HrObMInFMLEQUBOHQ"}

        s = ApiChannels().api_channels(url, headers)
        print("响应结果：", s.json())
        self.assertEqual(expect, s.json()['message'])
        self.assertEqual(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()
