#this file shoulb be replace and modified by main.py everytime it's runned
from os.path import getsize



cookies_info=THIS PART SHOULD BE REPLACED BY COOKIES_TEXT

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