import requests

headers={
    'Cookie':'_zap=bed9c2bc-2125-469a-a236-ca430fafd467; d_c0="APAar4HzxhGPTq7uG39OeQq7sRz4J4T2k_4=|1598189164"; _ga=GA1.2.1447417251.1598189167; _xsrf=1b7f5886-531d-4957-9caa-4504cc1bfbeb; _gid=GA1.2.644743472.1601019744; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1600765286,1601019743,1601021256,1601022422; capsion_ticket="2|1:0|10:1601022422|14:capsion_ticket|44:ZWI1YWE2NTUwODhiNGZhNjhlZmExZDM2MzVkOWFmM2Y=|b372a065594a163ffa1e9cb4255a1143bd346aafd6589ca8139be5616f258895"; _gat_gtag_UA_149949619_1=1; SESSIONID=XjBk2Lbc7AWhP4YLcix9c2q5vQS3rx2kv9DS5BA4FV6; JOID=W14SBUqSQVw1-tt-Pp0WBPt_J78hxSofWcCYHVytDwpcrecoc0roN2X91X440aQV0Eqn_k3VQRTY99aQUXTIoks=; osd=UF0dB0iZQlM3-NB9MZ8UD_hwJb0qxiUdW8ubEl6vBAlTr-UjcEXqNW7-2nw62qca0kis_ULXQx_b-NSSWnfHoEk=; z_c0="2|1:0|10:1601022445|4:z_c0|92:Mi4xN2N3WkJ3QUFBQUFBOEJxdmdmUEdFU1lBQUFCZ0FsVk43ZmRhWUFDbFRYT3loLTdMcmJHRm5fZm5naXQwOXVUcXhR|472dd09c39e4ec3706737d724f7409d88c9bf251afecc9984886edc87089ef7e"; unlock_ticket="ACAhGQDV6gwmAAAAYAJVTfWwbV8jO5lOae25SX4BYbyIY86vdaulRQ=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1601022446; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1601022447|1601019742',
    'Host':'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
r=requests.get('https://www.zhihu.com',headers=headers)
print(r.text)