#coding=utf-8
from user import user
from gradesList import gradesList as gl
import csv

print('Executing function')

if __name__ == "__main__":
	#new user
	user = user('402631767', 'qaz987wsx')
	try:
		links = user.getSemestersList()['links']#get links of pages
		cookie = user.getSemestersList()['cookie']#save cookie
	except:
		print('Error')

	#get list of grades
	gradesList = gl(links, cookie).getList()[0]

	with open("output.csv", "wd") as f:
		writer = csv.writer(f)
		writer.writerows(gradesList)
