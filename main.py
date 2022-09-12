'''
MIT License

Copyright (c) 2022 Danial Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
from pystyle import *
## from selenium import webdriver
## from selenium.webdriver.common.by import By
## from selenium.webdriver.support.ui import WebDriverWait
## from selenium.webdriver.support import expected_conditions as EC
## from selenium.webdriver.chrome.options import Options
## from selenium.webdriver.common.keys import Keys
## from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import keyboard as kb
import pyautogui as pag
import webbrowser as wb
import os


## try:
##     user_email = Write.Input("Email : ", Colors.red, interval=0)
##     user_pwd = Write.Input("Password : ", Colors.red, interval=0)
##     
##     
##     options = Options()
##     options.headless = False
##     options.page_load_strategy = 'eager'
##     
##     
##     
##     
##     
##     driver = webdriver.Chrome(options=options)
##     
##     driver.delete_all_cookies() ## Initialise the driver
##     driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
##         'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
##         '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
##         ## driver.maximize_window()
##     driver.implicitly_wait(15)
##     
##     wait = WebDriverWait(driver, 10)
##     
##     
##     loginBox = driver.find_element_by_xpath('//*[@id ="identifier"]')
##     loginBox.send_keys(user_email)
##     
##     nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
##     nextButton[0].click()
##     
##     
##     
##     
##     print('Login Successful...!!')
## except:
##     print('Login Failed')
## 
## Removing signin as google removed it and there is a long method that i dont want a user to have to setup/use
## email_field = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
## 
## for n in user_email+"\n":
##     email_field.send_keys(n)
##     sleep(0.5)
## sleep(2)
## email_field.send_keys(Keys.ENTER)
## 
## sleep(10)
## password_field = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
## 
## for n in user_pwd+"\n":
##     password_field.send_keys(n)
##     sleep(0.5)
## sleep(2)
## password_field.send_keys(Keys.ENTER)
## 


os.system('cls')
## Open gmail login


sleep(10)
print("Open your browser with gmail on home screen.")
while True:
    sleep(1)
    pag.moveTo(273, 152)
    pag.click()
    sleep(1)
    pag.moveTo()
    pag.click(429, 156)

