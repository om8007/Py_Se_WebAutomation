# -*- coding: utf-8 -*-
"""
Created on Tue Aug  13 12:13:22 2019
@author: om8007

Python-Selenium(Web Browser Automation framework) program to automate the process of jionet WiFi login
A suitable chromedriver(to open with Chrome) or firefox driver(to open with firefox) is required to run this program
chrome driver: https://sites.google.com/a/chromium.org/chromedriver/
firefox driver: https://github.com/mozilla/geckodriver/releases/
"""

def isConnected():
    try:
        driver.get("https://jionet2.jio.in:8443/")
        if driver.current_url=='https://jionet2.jio.in:8443/status':
            return True
    except Exception as e:
        print(e)

def start():
    print("Opening the browser...")
    print("Connecting to the WiFi login portal...")
    if isConnected():
        print("Already Connected!")
        driver.close()
        sys.exit()

def fill():
    #choose jio id option
    wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/section/div[2]/button'))).click()
    #Enter jio id
    inputId = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/section/div[1]/div[2]/label/span/input')))
    inputId.send_keys(id)
    #input password
    inputPass = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/section/div[2]/div[2]/label/span/input')))
    inputPass.send_keys(passw)
    #agree T&C
    wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/section/div[4]/div[2]/label/span[1]/span'))).click()
    #Submit
    wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/section/div[5]/div[2]/button'))).click()
    print('Login data submitted...',end="\n\n")

def msg():
    #data remaining
    data = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/section/div[1]/div[2]/ul/li/span/span[2]')))
    print(data.text)
    #continue btn click
    wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/section/div[2]/div[2]/button'))).click()
    #print("Continued..")
    time.sleep(2)



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.common.keys import Keys

#id = "<your_jio_id>"
#passw = "<your_password>"


driver = webdriver.Chrome(executable_path=r'Z:\python\driver\chromedriver.exe')     #local path to chromedriver
wait = WebDriverWait(driver,15)

start()
fill()
msg()
if isConnected():
    print("Connected!!! Enjoy :)")
    driver.close()

