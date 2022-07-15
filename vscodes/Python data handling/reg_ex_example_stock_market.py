import urllib.request
import re

base_url = "https://finance.naver.com/item/main.naver?code=005930"
html = urllib.request.urlopen(base_url)
html_contents = str(html.read().decode("ms949"))
# print(html_contents)

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
# print(stock_results)

samsung_stock = stock_results[0]
#print(samsung_stock)
#print(samsung_stock[1])
samsung_index = samsung_stock[1]

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])