# coding : utf-8
#�y�V�Œ����������L�[���[�h�Ō������ăV���b�v���Ɖ��i��\������

import requests
from bs4 import BeautifulSoup

keyword = input('�����������L�[���[�h����͂��Ă�������:\n')

url = 'https://search.rakuten.co.jp/search/mall/'+kw+'/'
html = requests.get(url)
soup = BeautifulSoup(html,'html.parser')
item = soup.select('.searchresultitem')

rank = 1

for item in items:
	title = item.select_one('.title').text.replace('\n','')
	price = item.select_one('.price').text.replace('\n','').replace(' ','')
	shopname = item.select_one(' .merchant').text.replace('\n','')
	print('�L�[���[�h�F�o�p���ʁF�o�p',format(kw,rank))
	print('���i���F�o�p'.format(title))
	print('�V���b�v���F�o�p���i�F�o�p'.format(shopname,price))
	print('*/'*20)
	rank = rank + 1
	
a = input('�������͂���ƏI�����܂�')