from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener

userName="userName"
passWord="passWord"
url="https://httpbin.org/post"

httpRealm = HTTPPasswordMgrWithDefaultRealm();
httpRealm.add_password(None,url,userName,passWord)

auth_handler = HTTPBasicAuthHandler(httpRealm)
opener=build_opener(auth_handler)
result = opener.open(url)
print(result.read())