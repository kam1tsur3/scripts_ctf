const crypto = require('crypto')

const HMAC_SHA256 = (key, data) => {
    const hash = crypto.createHmac('sha256', key).update(data).digest('base64')
    const hashNoPadding = hash.replace(/={1,2}$/, '')
    return hashNoPadding
}

const key = 'ilovepico'
//const jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ.t42p4AHef69Tyyi88U6+p0utZYYrg7mmCGhoAd7Zffs'
const jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicG9rZW1vbiJ9.5Y_gF7gkvENKJqkZ3APRbZf3s2JHOJ8azsitxgmvc6Q'

const splits = jwt.split('.')
const unsignedToken = [splits[0], splits[1]].join('.')
const signature = splits[2]

console.log(HMAC_SHA256(key, unsignedToken) === signature)
