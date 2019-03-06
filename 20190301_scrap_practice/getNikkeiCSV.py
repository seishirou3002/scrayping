# coding: UTF-8
#���o���ϊ����y�[�W�A�N�Z�X
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
		
	#csv��ǋL���[�h�ŊJ��
	f = open('nikkei_heikin.csv','a')
	writer = csv.writer(f,lineterminator='\n')
	
	while datetime.now().second != 59:
		time.sleep(1)
	#�����������I�����J��Ԃ��Ă��܂����߈�b�ҋ@
	time.sleep(1)
	
	#csv�ɋL�q�p���R�[�h
	csv_list = []
	
	time_ = datetime.now().strftime("%Y%m%d %H:%M:%S")
	
	#1�J�����ڂɎ��Ԃ�}��
	csv_list.append(time_)
	
	
	#�A�N�Z�X����URL
	url = "http://www.nikkei.com/markets/kabu/"

	#���o���ϊ����̃T�C�g��html���擾
	req = requests.get(url);
	soup = BeautifulSoup(req.content,"html.parser")

	#span�v�f�S�Ă𒊏o����
	span = soup.find_all("span")

	#print�G���[�΍�
	nikkei_means = ""
	#span�v�f����class="mkc-stock_prices"��T��
	for tag in span:
		try:
			string_ = tag.get("class").pop(0)
			#����m�F�p�f�o�b�N
			#print(tag.get("class"))
			
			if string_ in "mkc-stock_prices":
			
				nikkei_means = tag.string
				
				break
		except:
			
			pass
		
	print(time_, nikkei_means)
	
	#2�J�����ڂɓ��o���ϊ������L�^
	csv_list.append(nikkei_means)
	
	#csv�ɒǋL
	writer.writerow(csv_list)
	
	f.close()
