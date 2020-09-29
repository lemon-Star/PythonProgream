import requests

param={
    'callback':'jQuery172008198379407453582_1601021725944',
    'req_time':'1601021766682',
    'redirectURL':'http%3A%2F%2Fjf.10010.com%2F',
    'userName':'16603406060',
    'password':'02028a00ad5340aa73bffcfe31c2fae9d7558a7579088c5c3f30469f1a7d07c8513cf3fc17f502cf85291c877f4d97efa45c476365600e3ca9f2470212718a68e8758f1713ba7da97391c10c1c6de3f12309da22742d6e5e910289118a4831920bb9',
    'pwdType':'01',
    'productType':'01',
    'redirectType':'01',
    'rememberMe':'1',
    'verifyCKCode':'123422',
    '_':'1601021766694',
}
url='https://uac.10010.com/portal/Service/MallLogin'
r=requests.get(url,params=param)
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.content)
