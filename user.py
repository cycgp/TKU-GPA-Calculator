#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup as bs4

class user:
	def __init__(self, account, password):
		self.account = account
		self.password = password

	def getSemestersList(self):

		url = "https://portal.tku.edu.tw/NEAI/logineb.jsp"
		querystring = {"myurl":"http://portal.tku.edu.tw/aissinfo/emis/tmw0012.aspx"}
		COOKIE= "IV_JCT=%2FNEAI"

		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "e353341f-612f-1ef3-8b86-4b072935d1a2"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)

		JSESSIONID = bs4(response.text, 'html.parser').find('form', {'name':'eaiForm'})['action']
		COOKIE = response.headers['set-cookie'].split(' ')[0] +" "+ COOKIE
	    #
		url = "https://sso.tku.edu.tw"+JSESSIONID

		querystring = {"action":"EAI"}

		payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"myurl\"\r\n\r\nhttp://portal.tku.edu.tw/aissinfo/emis/tmw0012.aspx\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"ln\"\r\n\r\nzh_TW\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"embed\"\r\n\r\nNo\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"logintype\"\r\n\r\nlogineb\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+self.account+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+self.password+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"loginbtn\"\r\n\r\n登入\r\n-----011000010111000001101001--"
		headers = {
		    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "8b093830-abd4-9b13-aac0-30bf769888cd"
		    }

		response = requests.request("POST", url, data=payload, headers=headers, params=querystring, allow_redirects=False)
		try:
		    LOCATION = response.headers['location']
		except:
		    return "0"

		url = LOCATION

		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "0bbb3211-90bc-a2e6-13c3-b929abe8c02e"
		    }

		response = requests.request("GET", url, headers=headers, allow_redirects=False)

		PDHSESSIONID = response.headers['set-cookie'].split(' ')[0]
		PDID = response.headers['set-cookie'].split(' ')[3]

		COOKIE = COOKIE + "; " + PDHSESSIONID + " " + PDID

		url = "http://portal.tku.edu.tw/aissinfo/emis/tmw0012.aspx"

		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "936a496f-c519-8b01-c4d7-5d30a91a0acd"
		    }

		response = requests.request("GET", url, headers=headers, allow_redirects=False)

		ASPNETSessionId = response.headers['set-cookie'].split(' ')[0].split(';')[0]
		COOKIE = COOKIE + " " + ASPNETSessionId

		url = "http://portal.tku.edu.tw/aissinfo/emis/TMW0040.aspx"
		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "b6f22f9b-a357-519c-f63e-ab1292877821"
		    }

		response = requests.request("GET", url, headers=headers)

		url = "http://portal.tku.edu.tw/aissinfo/emis/TMWS030.aspx"

		headers = {
		    'cookie': COOKIE,
		    'cache-control': "no-cache",
		    'postman-token': "0f497fcb-4c53-6b2d-ab42-2229fbe2fff6"
		    }

		response = requests.request("GET", url, headers=headers)
		soup = bs4(response.text, 'html.parser')
		soup = soup.find('table', {'id':'DataGrid2'})
		soup = soup.find_all('a')
		soup = [link.get('href').encode('utf-8') for link in soup]

		return {'links': soup, 'cookie': COOKIE}
