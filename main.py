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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import keyboard as kb


options = Options()
options.headless = False
options.page_load_strategy = 'eager'

## options.add_experimental_option('excludeSwitches', ['enable-logging'])


user_email = Write.Input("Email : ", Colors.red, interval=0)
user_pwd = Write.Input("Password : ", Colors.red, interval=0)


driver = webdriver.Chrome(options=options) ## Initialise the driver
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S89338%3A1662998004781123&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWrfBuZ-D7ZE5VL5bFUQSDCmhI9fANP5uVDAupV_fsE4JnBZFtmcO7RTtihD0fFVecMNrxUiGw")
## driver.maximize_window()
wait = WebDriverWait(driver, 10)



email_field = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
email_field.send_keys(user_email)
kb.press('enter')
password_field = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
password_field.send_keys(user_pwd)
kb.press('enter')