import requests
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get("https://books.toscrape.com/",headers=head)
#状态码,如果是2开头的就请求成功
print(response.status_code)
#但是我们一般会这么写
if response.ok:
    print(response.text)
    #获取响应体内容
else:
    print("请求失败")