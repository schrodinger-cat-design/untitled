import requests
# response = requests.get("http://www.baidu.com")
# print(type(response.headers),response.headers) #获取请求头
# print(type(response.headers),response.headers) #获取响应头
# print(type(response.cookies),response.cookies)#获取响应cookie
# print(type(response.url),response.url) #获取响应url
# print(type(response.url),response.url) #获取请求url
url='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
url_get = requests.get(url) #获得网页url
print(url_get.content)
# url_post = requests.post(url)
# url_put = requests.put(url)
# url_delete = requests.delete(url)
# url_head = requests.head(url)
# url_options = requests.options(url)
with open('url_get.html','wb') as page:
    page.write(url_get.content)