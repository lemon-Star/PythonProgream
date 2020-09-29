import requests

headers={
    'User-Agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2473.116 Safari/537.36'
   # 'sec-fetch-dest': 'document',
   # 'sec-fetch-mode': 'navigate',
   # 'sec-fetch-site': 'none',
    #'sec-fetch-user': '1',
   # 'upgrade-insecure-requests': '1',
    #'cookie': '_zap=bed9c2bc-2125-469a-a236-ca430fafd467; d_c0="APAar4HzxhGPTq7uG39OeQq7sRz4J4T2k_4=|1598189164"; _ga=GA1.2.1447417251.1598189167; _xsrf=1b7f5886-531d-4957-9caa-4504cc1bfbeb; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1600306621,1600333991,1600765286,1601019743; capsion_ticket="2|1:0|10:1601019743|14:capsion_ticket|44:MWM2ZjUwYmZmMjI5NDMyOWJiOTIzNTQ4MWQ2MmM2ZGI=|3ed1f09340766b918e0b284f930daccd8ac27c065118b2f32ee35d0ae7ff1611"; _gid=GA1.2.644743472.1601019744; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1601021143; _gat_gtag_UA_149949619_1=1; SESSIONID=Kl4vFM4iLRfkpQ2OSypP7E55iCcB7pCk7YOY0P0YbrM; JOID=VlsUC0sDa8OHXD6Gew84kELewUNvTwX--R50sBtLPqflJGuzNtHEr9RfO416JNzIRAvJnShX8dpZDhLoHbpQaEs=; osd=W18WBkwOb8GKWzOCeQI_nUbczERiSwfz_hNwshZMM6PnKWy-MtPJqNlbOYB9KdjKSQzEmSpa9tddDB_vEL5SZUw=; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1601021148|1601019742'
    }
url='https://tieba.baidu.com'
r=requests.get(url)
with open('cc.text','wb') as  f:
    f.write(r.content)
print(r.text)
