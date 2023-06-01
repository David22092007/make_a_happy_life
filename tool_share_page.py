import requests,json,random,datetime;requests=requests.session()
count=0
sample_='''🐶	🐱	🐭	🐹
🐰	🦊	🐻	🐼
🐨	🐯	🦁	🐮
🐷	🐽	🐸	🐵
🙈	🙉	🙊	🐒
🐔	🐧	🐦	🐤
🐣	🐥	🦆	🦅
🦉	🦇	🐺	🐗
🐴	🦄	🐝	🐛
🦋	🐌	🐞	🐜
🦟	🦗	🕷	🕸
🦂	🐢	🐍	🦎
🦖	🦕	🐙	🦑
🦐	🦞	🦀	🐡
🐠	🐟	🐬	🐳
🐋	🦈	🐊	🐅
🐆	🦓	🦍	🦧
🐘	🦛	🦏	🐪
🐫	🦒	🦘	🐃
🐂	🐄	🐎	🐖
🐏	🐑	🦙	🐐
🦌	🐕	🐩	🦮
 	🐓	🦃🦚	🦜	🦢
	🦩'''
sample_=sample_.split()
cookie=input('Nhập cookie :');link_s=input('Nhâp link : ')
def text():
    global sample_
    sample=str(random.choices(sample_,k=10))+'\n'+str(random.choices(sample_,k=10))+'\t'+str(random.choices(sample_,k=10))+'\n'+str(random.choices(sample_,k=10))+str(random.choices(sample_,k=10))+'\n'+str(random.choices(sample_,k=10))+'\t'+str(random.choices(sample_,k=10))+'\n'+str(random.choices(sample_,k=10))+str(random.choices(sample_,k=10))+'\n'+str(random.choices(sample_,k=10))+'\t'+str(random.choices(sample_,k=10))+'\n'+str(random.choices(sample_,k=10))
    return sample;
while True:

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
        'authority': 'graph.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # Requests sorts cookies= alphabetically
        'cookie': cookie,
        'origin': 'https://developers.facebook.com',
        'pragma': 'no-cache',
        'referer': 'https://www.facebook.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    params = {
        'access_token': access_token,
        'debug': 'all',
        'fields': 'access_token',
        'limit': '999999999999999999999999999999999999999999999999',
        'format': 'json',
        'method': 'get',
        'pretty': '0',
        'suppress_http_code': '1',
        'transport': 'cors',
    }

    rsp = requests.get('https://graph.facebook.com/v15.0/me/accounts', params=params, headers=headers).text
    data=json.loads(rsp)['data']
    for i in data:
        count=count+1
        token=i['access_token']
        params = {
            'message': text(),
            'link': link_s,
            'access_token': token,

        }
        rsp = requests.post('https://graph.facebook.com/v15.0/me/feed', params=params,headers=headers).text
        try:
            check=json.loads(rsp)['id']
            f=open('list_data.txt','a')
            f.write(check+str('\n'))
            print ('[',datetime.datetime.now(),']',check)
        except:
            print ('\n Lỗi SHARE')
        if count==10:
            time.sleep(60)
    
