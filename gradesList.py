#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup as bs4

class gradesList:
	def __init__(self, links, cookie):
		self.links = links
		self.cookie = cookie

	def getList(self):

		semesGradesList = []
		gradesList = []
		url = 'http://sso.tku.edu.tw/aissinfo/emis/'
		links = self.links

		COOKIE= self.cookie

		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "e353341f-612f-1ef3-8b86-4b072935d1a2"
		    }

		for link in links:
			response = requests.request("GET", url+link.decode('utf-8'), headers=headers)
			soup = bs4(response.text, 'html.parser')
			tableSoup = soup.find('table', {'id':'DataGrid3'})
			trSoup = tableSoup.find_all('tr')[1:]
			gradesInfoList = [gradesInfo.find_all('td')[:-1] for gradesInfo in trSoup]

			for gradesInfo in gradesInfoList:
				i = gradesInfoList.index(gradesInfo)
				for grades in gradesInfo:
					j = gradesInfo.index(grades)
					grades = grades.getText().strip()
					gradesInfoList[i][j] = grades.encode('utf-8')
				gradesList.append(gradesInfo)
			semesGradesList.append(gradesInfoList)

		return [gradesList, semesGradesList]
