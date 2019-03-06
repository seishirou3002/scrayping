# coding: UTF-8
#日経平均株価ページアクセス
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

while True:

	if datetime.now().minute != 59:
		time.sleep(58)
		continue
		
	#csvを追記モードで開く
	f = open('nikkei_heikin.csv','a')
	writer = csv.writer(f,lineterminator='\n')
	
	while datetime.now().second != 59:
		time.sleep(1)
	#処理が早く終わり二回繰り返してしまうため一秒待機
	time.sleep(1)
	
	#csvに記述用レコード
	csv_list = []
	
	time_ = datetime.now().strftime("%Y%m%d %H:%M:%S")
	
	#1カラム目に時間を挿入
	csv_list.append(time_)
	
	
	#アクセスするURL
	url = "http://www.nikkei.com/markets/kabu/"

	#日経平均株価のサイトのhtmlを取得
	req = requests.get(url);
	soup = BeautifulSoup(req.content,"html.parser")

	#span要素全てを抽出する
	span = soup.find_all("span")

	#printエラー対策
	nikkei_means = ""
	#span要素からclass="mkc-stock_prices"を探索
	for tag in span:
		try:
			string_ = tag.get("class").pop(0)
			#動作確認用デバック
			#print(tag.get("class"))
			
			if string_ in "mkc-stock_prices":
			
				nikkei_means = tag.string
				
				break
		except:
			
			pass
		
	print(time_, nikkei_means)
	
	#2カラム目に日経平均株価を記録
	csv_list.append(nikkei_means)
	
	#csvに追記
	writer.writerow(csv_list)
	
	f.close()
