'''
目标：完成登录业务层实现
'''

#导包 unittest ApiLogin
import unittest

from parameterized import parameterized

from api.api_login import ApiLogin
from tools.read_json import read_json


def get_data():
    data =read_json("login.json")
    #新建空列表添加读取数据
    arrs=[]
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect"),
                 data.get("status_code")))
    return arrs



#新建测试类
class TestLogin(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,expect,status_code):
        #暂时存放数据 url mobile code
        # url ="http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile ='13249704047'
        # code ="175647"

        #调用登录方法
        s = ApiLogin().api_post_login(url,mobile,code)
        #断言 响应信息及状态码
        print("查看响应结果：",s.json())
        # self.assertEqual("OK",s.json()['message'])
        self.assertEqual(expect,s.json()['message'])
        # self.assertEqual(201,s.status_code)
        self.assertEqual(status_code,s.status_code)

if __name__ == '__main__':
    unittest.main()

'''
'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjIzMDUxMzcsInVzZXJfaWQiOjEzOTg2NDQ1ODU4NjkwODI2MjQsInJlZnJlc2giOmZhbHNlfQ.L5jfzIGyvsM6fb2bIYguD_CP__HrObMInFMLEQUBOHQ'

'refresh_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjM1MDc1MzcsInVzZXJfaWQiOjEzOTg2NDQ1ODU4NjkwODI2MjQsInJlZnJlc2giOnRydWV9.b03dsvyiEgll0PunQSIbNk1k9fgURIxQ8TVC2zzFeMk'
'''