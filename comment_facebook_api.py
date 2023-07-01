def comment_sourse(cookie,acces_token,message_text,i):
    headers = {
        'authority': 'graph.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'origin': 'https://developers.facebook.com',
        'pragma': 'no-cache',
        'referer': 'https://developers.facebook.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0',
    }

    params = {
        'access_token': acces_token,
    }

    data = {
        'debug': 'all',
        'format': 'json',
        'message': message_text,
        'method': 'post',
        'pretty': '0',
        'suppress_http_code': '1',
        'transport': 'cors',
    }

    response = requests.post(
        'https://graph.facebook.com/v17.0/125703577039251_591735049739827/comments',
        params=params,
        headers=headers,
        data=data,
    ).text
    print (response,i)
