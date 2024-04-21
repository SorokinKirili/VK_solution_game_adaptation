import os
import time
import winreg 
os.system("pip install selenium")
os.system("pip install pyautogui")

import selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

fullpath=os.path.dirname(os.path.abspath(__file__))
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": fullpath,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(chrome_options)
driver.get("https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=1")
element = driver.find_element( By.ID , "uc-download-link")
element.click()
time.sleep(5)

# while not os.path.isfile("settings.reg"):
#     time.sleep(1)
driver.close()
fullpath+='\settings.reg'
f=open(fullpath,'r')
lines=[]
while True:
    line= f.readline()
    line=line.replace('\x00','')
    if not line:
        break
    if len(line)>2:
        lines.append(line)
key1=''
sub_key=''
typest=''
value=''
got=0
for string in lines:
    i=0
    while i<len(string):
        if string[i]=='\\':
            n=i+1
            while string[n]!=']':
                key1+=string[n]
                n+=1
            i=n
            key=winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,key1,access=winreg.KEY_SET_VALUE)
        if string[i]=='"':
            got=1
            sub_key=''
            n=i+1
            while True:
                if string[n]=='"':
                    break
                else:
                    sub_key+=string[n]
                    n+=1
            i=n
        if string[i]=='=':
            typest=''
            n=i+1
            while True:
                if string[n]==':':
                    break
                else:
                    typest+=string[n]
                    n+=1
            i=n   
        if string[i]==':':
            value=''
            n=i+1
            while n<len(string):
                value+=string[n]
                n+=1
            value=int(value)
            i=n
        i+=1
    if got==1:
        if typest=='dword':
            type = winreg.REG_DWORD
        winreg.SetValueEx(key, sub_key, 0, type, value)
        print('done') 
winreg.CloseKey(key)

driver = webdriver.Chrome(chrome_options)
driver.get('steam://rungameid/1568590')
time.sleep(1)
pyautogui.press('left')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
driver.close()
time.sleep(30)