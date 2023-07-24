import requests,json
def headers(cookie):
    
    headers = {
        'authority': 'graph.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,#'sb=Vui9ZOuU04cmO1mCsICjSNNO; datr=Vui9ZGHHgJsfWe3TdswMX5v4; c_user=100053657943977; xs=43%3Aephsziay54K0PA%3A2%3A1690167395%3A-1%3A14449; fr=0QqVRQJTSha05g2UZ.AWWbAPPg7RY44mm7VxJhczYXPVQ.BkvehW.xZ.AAA.0.0.Bkve7L.AWVQMhBmr80; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1690169064019%2C%22v%22%3A1%7D; locale=vi_VN; fbl_st=101532860%3BT%3A28169490; wl_cbv=v2%3Bclient_version%3A2294%3Btimestamp%3A1690169408; fbl_cs=AhAJNc3SUtRhfXvplrtlz7aSGERmaEJSNklBUzNhYVlxamp5ell4bm13bQ; fbl_ci=1123931708565701; wd=1001x783; usida=eyJ2ZXIiOjEsImlkIjoiQXJ5YTVveGV2bmJyYiIsInRpbWUiOjE2OTAxNzAxMzh9',
        'origin': 'https://developers.facebook.com',
        'referer': 'https://developers.facebook.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    return headers
def main_sourse(headers,token_page_list):
    for i in token_page_list:
        access_token=i['access_token']  
        print (i['id'])
        try:
            params = {
                'access_token': access_token,
            }

            data = {
                'debug': 'all',
                'format': 'json',
                'method': 'post',
                'pretty': '0',
                'suppress_http_code': '1',
                'transport': 'cors',
                'url': 'https://source.unsplash.com/featured/?quote',
            }

            response = requests.post('https://graph.facebook.com/v17.0/me/photos', params=params, headers=headers, data=data)
            params = {
                'access_token': access_token,
            }

            data = {
                'cover': '293003479915194',
                'debug': 'all',
                'format': 'json',
                'method': 'post',
                'pretty': '0',
                'suppress_http_code': '1',
                'transport': 'cors',
            }

            response = requests.post('https://graph.facebook.com/v17.0/me', params=params, headers=headers, data=data).text
            json.loads(response)['success']
        except:
            token_page_list.append(i)

          
def get_token_user(headers):
    home_business = requests.get('https://business.facebook.com/content_management', headers=headers).text
    reg_token = home_business.split('EAAG')[1].split('","')[0]
    token="EAAG"+str(reg_token)
    return token  
def get_token_page_list(headers,token_user,sll):
    response = requests.get(
        'https://graph.facebook.com/v17.0/me?access_token='+str(token_user)+'&debug=all&fields=accounts.limit('+str(sll)+')%7Baccess_token%7D&format=json&method=get&pretty=0&suppress_http_code=1&transport=cors',
        headers=headers,
    ).text
    list_=json.loads(response)['accounts']['data']
    return list_    
cookie=input('COOKIE? ')  
sll=999999999999999999999999999999999999999999999999999999      
headers=headers(cookie)
token_user=get_token_user(headers)  
token_page_list=get_token_page_list(headers,token_user,sll)  
main_sourse(headers,token_page_list)
