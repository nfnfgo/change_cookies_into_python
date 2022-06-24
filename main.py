import subprocess
import time
import os
import sys

#read the cookies text from txt file.
with open('cookies.txt','r') as f:
    cookies_text=f.read()

#delete the space and enter
cookies_text=cookies_text.replace(' ','')
cookies_text=cookies_text.replace('\n','')
#replace true and false into PYTHON type
cookies_text=cookies_text.replace('true','True')
cookies_text=cookies_text.replace('false','False')

#use the text info to construct the python file for next step
with open('next.py') as f:
    py_text=f.read()

#replace the dict with cookies_text
py_text=py_text.replace('THIS PART SHOULD BE REPLACED BY COOKIES_TEXT',cookies_text)

#save the py file as 'next_run.py'
with open('next_run.py','w') as f:
    f.write(py_text)

#run the next_run.py
os.system('python3 next_run.py')