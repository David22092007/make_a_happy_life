import threading,time,os
from sourse import runtext as rt
import requests ;requests=requests.session()
check_alive_cookie=input('Continue using old cookie sue ? :')
if check_alive_cookie=='No' or check_alive_cookie=='no':
    try:
        os.remove('cookie.txt')
    except:        
        None
open_=open('cookie.txt','a')
open_.close()
a=open('cookie.txt','r')
a_=a.read().split('\n')
i=1
if a_==['']:
    while i:       
        f=open('cookie.txt','a')
        
        cookie=input(f'Nhập cookie thứ [{i}] :')

        f.write(str(cookie)+'\n') 
      
        if cookie=='':
            exit()
        i=i+1    
id_share=input('Nhập id share : ')
if id_share==['']:    
    exit()
else:    
    a=open('cookie.txt','r')
            
    a_=a.read().split('\n')

    while True:    
        for a in a_:
            try:
                id_share=rt(a,id_share)
            except:
                continue
