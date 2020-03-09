# -*- coding: utf-8 -*-
"""
Created on Mon 9 March,2020

@author: om8007

Download suitable chrome driver from https://chromedriver.chromium.org/downloads
"""

from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from random import randint

def loadWebsite():
    driver.maximize_window()
    driver.get("https://www.google.com")
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')))
    search_box.send_keys("holi" + Keys.ENTER)
    canvas = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rhs"]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/canvas')))
    canvas.click()
    i=0
    while i<200:                                                                      # no of clicks = 200
        x = randint(5, 1895)
        y = randint(85,1040)
        pyautogui.click(x, y)
        time.sleep(0.5)
        i+=1;

#====# main #====#
if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'Z:\python\driver\chromedriver80.exe')     # local path to chromedriver suitable for your chrome version
    wait = WebDriverWait(driver,20)

    loadWebsite()

    driver.close()

