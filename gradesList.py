#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup as bs4

class gradesList:
	def __init__(self, links, cookie):
		self.links = links
		self.cookie = cookie

	def getList(self):

		url = 'http://sso.tku.edu.tw/aissinfo/emis/'
		links = self.links

		COOKIE= self.cookie

		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "e353341f-612f-1ef3-8b86-4b072935d1a2"
		    }

		response = requests.request("GET", url+links[0], headers=headers)
		soup = bs4(response.text, 'html.parser')
		soup = soup.find('table', {'id':'DataGrid3'})
		soup = soup.find_all('td')

		return soup
