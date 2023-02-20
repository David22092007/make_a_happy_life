import requests,datetime,time,random,os,json;from gettoken import runtext as gt;from autopostpage_facebook_MOMO_TOOL import upload_page;requests=requests.session()
cookie=input('COOKIE =? ')
try:
    time_=int(input('Nhập time upload page : '))
except:
    None
try:    
    check_chooise=int(input('Bạn Muốn Upload Page Không 0/1: '))
except:   
    check_chooise=0
try:
    time_delay_register_page=int(input('Độ trễ thời gian register_page :'))
except:
    time_delay_register_page=500
access_token_user=gt(cookie)
if check_chooise >0:
    try:
        sll=int(input('Số Page Muốn Úp : '))
    except:
        sll='9999999999999999999999999999999999999999999999999999999999999999999999999999'
    upload_page(cookie,time_,access_token_user,sll)
else:
    os.system("cls")
headers = {
    'authority': 'graph.facebook.com',
    'accept': '*/*',
    'cookie': cookie,
    'origin': 'https://business.facebook.com',
    'pragma': 'no-cache',
    'referer': 'https://www.facebook.com',
}
params = {
    'access_token': access_token_user,
    'debug': 'all',
    'fields': 'access_token',
    'limit': '9999999999999999999999999999999999999999999999999999999999999999999999999999',
    'format': 'json',
    'method': 'get',
    'pretty': '0',
    'suppress_http_code': '1',
    'transport': 'cors',
}
list_ = json.loads(requests.get(f'https://graph.facebook.com/v15.0/me/accounts', params=params, headers=headers).text)['data']
while True:
    for i in list_:
        access_token=i['access_token']
        id_page=i['id']
        while True:
            params = {
                'access_token': access_token,
            }
            try:
                len_ = json.loads(requests.get(f'https://graph.facebook.com/v15.0/{id_page}/locations', params=params, headers=headers).text)['data'];a=len(len_)+random.randint(2,9999)
            except:
                None
            try:    
                data = {
                    'id': id_page,
                    'ignore_warnings': 'true',
                    'locale': 'vi_VN',
                    'location': '{"city_id":2584768,"latitude":"15.123755","longitude":"108.'+str(random.randint(100,12839123898231983129))+'","street":"'+str(random.randint(100,12839123898231983129))+' Adam ","zip":"199"}',
                    'method': 'post',
                    'phone': '+84983717317',
                    'pickup_options': '["in_store","curbside"]',
                    'place_topics': '["2700"]',
                    'store_name': (datetime.date.today()).strftime("%d/%m/%Y")+str((datetime.datetime.now())),
                    'store_number': a,
                }
                rsp = json.loads(requests.post(f'https://graph.facebook.com/v14.0/{id_page}/locations', params=params, headers=headers, data=data).text);id_page_location=rsp['id'];print('[',id_page,']',id_page_location);a=open('list_id.txt','a');a.write(str(id_page_location)+'\n')
                time.sleep(time_delay_register_page)
            except:    
                print ('FAIL --'+str(datetime.datetime.now())+'==>Page Hiện Tại : '+str(len(len_)))
                if len(len_) >0 :
                    a=open('list_mother_page.txt','a')
                    a.write(id_page+'\n')                   
                break
    
