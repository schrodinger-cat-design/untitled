import requests
#获取网页源代码
url_get = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
#把url_get内容以字符串的形式返回
html = url_get.text
#检查请求是否正确反应
print('响应状态码：%s' %(url_get.status_code))
#打印网页源代码
print(html)