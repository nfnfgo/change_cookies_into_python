#this file shoulb be replace and modified by main.py everytime it's runned

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