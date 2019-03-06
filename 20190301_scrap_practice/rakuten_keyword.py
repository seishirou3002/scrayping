# coding : utf-8
#楽天で調査したいキーワードで検索してショップ名と価格を表示する

import requests
from bs4 import BeautifulSoup

keyword = input('調査したいキーワードを入力してください:\n')

url = 'https://search.rakuten.co.jp/search/mall/'+kw+'/'
html = requests.get(url)
soup = BeautifulSoup(html,'html.parser')
item = soup.select('.searchresultitem')

rank = 1

for item in items:
	title = item.select_one('.title').text.replace('\n','')
	price = item.select_one('.price').text.replace('\n','').replace(' ','')
	shopname = item.select_one(' .merchant').text.replace('\n','')
	print('キーワード：｛｝順位：｛｝',format(kw,rank))
	print('商品名：｛｝'.format(title))
	print('ショップ名：｛｝価格：｛｝'.format(shopname,price))
	print('*/'*20)
	rank = rank + 1
	
a = input('何か入力すると終了します')