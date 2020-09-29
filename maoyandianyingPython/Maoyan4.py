import requests
import re
import json

#抓取猫眼电影信息
def get_one_page(url):
    headers={
        'Cookie':'__mta=121413687.1601257460142.1601257487449.1601259941422.6; uuid_n_v=v1; uuid=200E9EF0012C11EBAAFDB3416A6201C851509549A091425AAAEBC1066C5C8C78; _csrf=e2e91ac0b3572e2fdf327e2d7f6375c995b0915df7791834d52ba9a6e9b5910f; mojo-uuid=1222b7cfaeabd82ca08d93e22852a6bc; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601257460; _lxsdk_cuid=174d261d160c8-06d2f4efa09b08-316b7004-13c680-174d261d160c8; _lxsdk=200E9EF0012C11EBAAFDB3416A6201C851509549A091425AAAEBC1066C5C8C78; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601259941; _lxsdk_s=174d2be6241-481-b8e-047%7C%7C1',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    respinse=requests.get(url,headers=headers)
    if respinse.status_code == 200:
        html=respinse.text
        result = re.findall(
            '<dd>.*?board-index.*?">(.*?)</i>.*?<a.*?title="(.*?)".*?<img.*?src="(.*?)".*?<img.*?data-src="(.*?)".*?class="board-img".*?',
            html, re.S)
        return result;
    return None

def main():
    url='https://maoyan.com/board/4'
    html=get_one_page(url)
    return html


def write_to_file(content,fileName):
    with open(fileName,'a',encoding='utf-8') as f:
        for data in content:
            f.write('电影排名：' + data[0] + '\n')
            f.write('电影名称：' + data[1] + '\n')
            f.write('图片：' + data[2] + '\n')
            f.write('电影链接：' + data[3] + '\n')
            f.write('--------------------' + '\n')


html=main();
write_to_file(html,'Maopyan4.txt')