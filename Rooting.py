import requests
import json
from requests.api import request
from requests.models import Response


url = 'http://86.48.0.204:919//main'

r = requests.session()

green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color = "\033[1;33;40m"
end_banner_color = "\33[00m"

print (detect_color+"""
    ███████ ███████  ██████  ███    ███               ██████   ██████   ██████  ████████
       ██   ██       ██   ██ ████  ████               ██   ██ ██    ██ ██    ██    ██
       ██   █████    ███████ ██ ████ ██     █████     ██████  ██    ██ ██    ██    ██   
       ██   ██       ██   ██ ██  ██  ██               ██   ██ ██    ██ ██    ██    ██ 
       ██   ███████  ██   ██ ██      ██               ██   ██  ██████   ██████     ██
      
                                                                                     
     ██████  ██ ██████  ██████         █████  ██      ██████  ██    ██  ██████  ██        
     ██   ██ ██      ██ ██   ██       ██   ██ ██      ██   ██ ██    ██ ██    ██ ██        
     ██████  ██  █████  ██   ██ █████ ███████ ██      ██████  ██    ██ ██    ██ ██        
     ██   ██ ██ ██      ██   ██       ██   ██ ██      ██   ██ ██    ██ ██ ▄▄ ██ ██        
     ██   ██ ██ ███████ ██████        ██   ██ ███████ ██   ██  ██████   ██████  ██       
                                                                   ▀▀       
                                                                                                                                               
                                                                                           
""")
print (end_banner_color + '''
==============================================
Powerd By TEAM-ROOT Created By : RiadAlruqi 
==============================================
''')


header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "%D9%86%D9%85%D8%A8%D8%B1%D8%A8%D9%88%D9%83%20%D8%A7%D9%84%D8%AE%D9%84%D9%8A%D8%AC%201/3.3 CFNetwork/1240.0.4 Darwin/20.5.0",
        "Accept-Encoding": "gzip, deflate",
        "Host": "86.48.0.204:919",
        "Accept": "*/*",
"Accept-Language": "ar",
"Authorization": "Basic aW9zYWRtaW46cGFzc3BvcmQ=",
"token": "pcfgv64567ko1",
"Content-Length":"19",
}
number = input("ادخل الرقم بدون 0 => ")


json = {
    "number": "966"+number,
}

response = requests.post(url, data=json, headers=header).text


print(response) 
#https://discord.gg/4WDRhQft
