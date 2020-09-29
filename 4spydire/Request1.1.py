import urllib.request

request = urllib.request.Request("https://python.org")

print(type(request))
response = urllib.request.urlopen(request)