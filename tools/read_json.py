#导包 json
import json
#打开json文件取文件流
# with open("../data/login.json","r",encoding="utf-8") as f :
#     # 调用 load方法加载文件流
#     data =json.load(f)
#     print(data)

#函数封装
def read_json(filename):
    filepath ="../data/"+filename
    with open(filepath,"r",encoding="utf-8") as f :
        # 调用 load方法加载文件流
        return json.load(f)

'''
    1.未经过封装无法在别的模块内使用——-进行封装
    2.数据存储文件有好几个，如果写死，在读取别的文件时无法使用--使用参数替换静态写死的文件名
    3.预期格式为列表嵌套元组[(url,mobile,code)],目前返回字典————读取字典内容，并添加到新的列表
'''

if __name__ =="__main__":
    # print(read_json("login.json"))
    data =read_json("login.json")
    #新建空列表添加读取数据
    arrs=[]
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect"),
                 data.get("status_code")))
    print(arrs)

