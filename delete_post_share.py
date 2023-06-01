import requests,queue,threading
import datetime
cookie=input('')
q=queue.Queue()
def get_token(cookie):
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
    return ("EAAG"+str(reg_token));
    
def main():
    global cookie,q,token
    while not q.empty():
        id_=q.get()
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

        response = requests.delete('https://graph.facebook.com/v16.0/'+id_, params=params,headers=headers).text
        try:
            json.loads(response)['success']
            print (datetime.datetime.now())
            
        except:
            print ('Fail')
            q.put(id_)
        
def get_date_line():
    global q
    a=open('list_data.txt','r')
    for i in a.readlines():
        q.put(i.replace('\n',''))

token=get_token(cookie)
get_date_line()
for i in range(5):
    threading.Thread(target=main).start()   
