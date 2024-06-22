import requests,json,time
from datetime import datetime
requests=requests.session()
def convert_to_json_string(data_str):
    data_dict = eval(data_str)
    json_string = json.dumps(data_dict)
    return json_string
response=requests.get('https://raw.githubusercontent.com/David22092007/Auto-Tik-Tok-TDS-/main/readme.txt').text
for i in response.split('\n'):
    if i.find('id_group=') >=0:
        id_group=(i.split('=')[1]).replace('\n','')
    if i.find('cookie=') >=0:
        cookie=(i.replace('cookie=','')).replace('\n','')
    if i.find('time_repeat') >=0:
        time_repeat=int((i.replace('time_repeat=','')).replace('\n',''))
    if i.find('times') >=0:
        count_per_day=int((i.replace('times=','')).replace('\n',''))
    if i.find('count') >=0:
        count=int((i.replace('count=','')).replace('\n',''))
header_ = {
    'authority': 'business.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': cookie,
    'referer': 'https://www.facebook.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',

}

home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
reg_token = home_business.split('EAAG')[1].split('","')[0]
access_token="EAAG"+str(reg_token)
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': cookie,
    'origin': 'https://developers.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://developers.facebook.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}
params = {
    'access_token': access_token,
    'debug': 'all',
    'format': 'json',
    'method': 'get',
    'origin_graph_explorer': '1',
    'pretty': '0',
    'suppress_http_code': '1',
    'transport': 'cors',
}
response = requests.get('https://graph.facebook.com/v20.0/'+str(id_group)+'?fields=feed{comments}', params=params, headers=headers).text 
date=(str(datetime.now()).split(' '))[0]
with open ("count.txt",'r') as f:
  data=(json.loads(f.readline()))
  f.close() 
for i in json.loads(response)['feed']['data']:
    cctv_cam=True
    try:
        count=int(data['data']["date-record"][date]['count'])
        if int(data['data']["date-record"][date]['count']) >= count_per_day:
            exit()
    except Exception as e:
        None
    try:
        id_comment=(i['comments']['data'][0]['id'])
    except Exception as e:
        None 
    for lk in data['data']['id_post']:
        if int(id_comment) == int(lk):
            cctv_cam=False
            break      
    while cctv_cam:        
        response = requests.post('https://graph.facebook.com/v20.0/'+str(id_comment)+'/likes?access_token='+str(access_token), headers=headers).text 
        while json.loads(response)['success']:
            count+=1
            data['data']['id_post'].append(id_comment)
            data['data']["date-record"].update({date:{'count':count}})
            with open('count.txt','w') as f:
                f.write(convert_to_json_string(str(data)))
                f.close()
            break           
        time.sleep(time_repeat)
        break
        

    
