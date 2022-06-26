#this file shoulb be replace and modified by main.py everytime it's runned
from os.path import getsize



cookies_info=[{"domain":".youdao.com","hostOnly":False,"httpOnly":False,"name":"DICT_UGC","path":"/","sameSite":"unspecified","secure":False,"session":True,"storeId":"0","value":"be3af0da19b5c5e6aa4e17bd8d90b28a|","id":1},{"domain":".youdao.com","hostOnly":False,"httpOnly":False,"name":"JSESSIONID","path":"/","sameSite":"unspecified","secure":False,"session":True,"storeId":"0","value":"abc7nscIMUY4P9aJ-Jtgy","id":2},{"domain":".youdao.com","expirationDate":2602118096.003096,"hostOnly":False,"httpOnly":False,"name":"OUTFOX_SEARCH_USER_ID","path":"/","sameSite":"unspecified","secure":False,"session":False,"storeId":"0","value":"-1981012200@10.110.96.153","id":3},{"domain":".youdao.com","expirationDate":1719110096,"hostOnly":False,"httpOnly":False,"name":"OUTFOX_SEARCH_USER_ID_NCOO","path":"/","sameSite":"unspecified","secure":False,"session":False,"storeId":"0","value":"429013887.882062","id":4},{"domain":"www.youdao.com","hostOnly":True,"httpOnly":False,"name":"___rl__test__cookies","path":"/","sameSite":"unspecified","secure":False,"session":True,"storeId":"0","value":"1656038100098","id":5}]

#initialize cookie dict
cookies_dict={}

#'s' means single
for s_cookies_info in cookies_info:
    name=s_cookies_info['name']
    value=s_cookies_info['value']
    cookies_dict[name]=value

#print it out and save it to txt file as 'cookies_dict.txt'
print('cookies_dict:',cookies_dict)
with open('cookies_dict.txt','w') as f:
    f.write(str(cookies_dict))

#construct the meta info
cookies_len=len(cookies_dict)
text_size=getsize('cookies.txt')
dict_size=getsize('cookies_dict.txt')
#construct the meta_text
meta_text='————————————————\n'
meta_text+='Cookies Amount: '+str(cookies_len)+'\n'
meta_text+='Cookies File Size: '+format(text_size/1024,'.2f')+'KB\n'
meta_text+='Cookies Dict File Size: '+format(dict_size/1024,'.2f')+'KB\n'
print(meta_text)