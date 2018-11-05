import urllib3
import urllib
import re
import csv
import sys
import requests
from bs4 import BeautifulSoup
import os
from xlwt import *
def getHtml(url):
	r = requests.get(url)
	s = r.status_code
	if(s==404):
		print("404")
	return r.content
if __name__ == '__main__':
	url = "http://120.78.162.102/ranklistnew.php"
	csvfile = open('user.csv', 'w', newline='')
	writer = csv.writer(csvfile)
	writer.writerow(['学号','用户名','刷题数'])
	content = getHtml(url)
	soup = BeautifulSoup(content, 'html.parser')
	div_people_list = soup.find('div', attrs={'id': 'main'})
	name_s = div_people_list.find_all_next('div', attrs={'class': 'center'})
	i=0
	a = []
	s = []
	for name in name_s:
		a.append(name.get_text())
	for i in range(1,1200,4):
		s.append(d)
	for it in s:
		writer.writerow(it)
csvfile.close()

