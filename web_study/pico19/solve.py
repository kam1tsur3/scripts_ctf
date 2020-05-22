#!/usr/bin/python3

import jwt
#header = "{\"typ\":\"JWT\",\"alg\":\"HS256\"}"
#data = "{\"user\":\"admin\"}"
encoded = jwt.encode({'user': 'admin'}, 'ilovepico', algorithm='HS256')
print(encoded)
