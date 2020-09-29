from urllib.parse import parse_qs

#反序列化操作
queryParams="userName=bob&passWord=a111111"
query=parse_qs(queryParams)
print(query)


