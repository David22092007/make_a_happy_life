import requests ;requests=requests.session()
import datetime,json,threading,time
def runtext(cookie,id_share):
    count=0
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
    token="EAAG"+str(reg_token)
    list_=[cookie,id_share,token]
    def main(list_):
        cookie,id_share,token=list_[0],list_[1],list_[2]
        for i in range(10):
            headers = {
                'authority': 'graph.facebook.com',
                'accept': '*/*',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cache-control': 'no-cache',
                # Requests sorts cookies= alphabetically
                'cookie': cookie,
                'origin': 'https://developers.facebook.com',
                'pragma': 'no-cache',
                'referer': 'https://www.facebook.com',  
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
            }

            params = {
                'access_token': token,
            }

            data = {
                'debug': 'all',
                'format': 'json',
                'link': 'https://m.facebook.com/'+str(id_share),
                'method': 'post',
                'pretty': '0',
                'published': '0',
                'suppress_http_code': '1',
                'transport': 'cors',
            }
            try:
                rsp = requests.post('https://graph.facebook.com/v15.0/me/feed', params=params, headers=headers, data=data,timeout=3)
            except:
                continue
            try:
                id_share=json.loads(rsp.text)['id']
                t = datetime.datetime.now()
                print (f'[{t}] : '+str(id_share))
            except:
                print (rsp.text)
                time.sleep(10)
                rsp.close()
                time.sleep(500)
                exit()
                
        time.sleep(60)
        return id_share
    def runtest(x):
        id_share=main(list_)
        return id_share
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=runtest,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return id_share         
