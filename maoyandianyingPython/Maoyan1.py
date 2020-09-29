import requests

#抓取猫眼电影信息
def get_one_page(url):
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    respinse=requests.get(url,headers=headers)
    if respinse.status_code == 200:
        return respinse.text
    return None

def main():
    url='https://maoyan.com/board/4'
    html=get_one_page(url)
    print(html)

main();