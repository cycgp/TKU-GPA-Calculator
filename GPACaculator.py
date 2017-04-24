#coding=utf-8
from user import user
from gradesList import gradesList as gl

print('Executing function')

if __name__ == "__main__":
	#new user
	user = user('402631757', 'qaz987wsx')
	links = user.getSemestersList()['links']#get links of pages
	cookie = user.getSemestersList()['cookie']#save cookie

	#get list of grades
	gradesList = gl(links, cookie).getList()

	for grades in gradesList:
		print(grades.encode('utf-8'))
