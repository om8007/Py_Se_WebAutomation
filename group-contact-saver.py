# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:30:27 2019

@author: om8007
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path=r'Z:\python\driver\geckodriver.exe')  #local path to your firefox driver

driver.get("https:/web.whatsapp.com/")
wait = WebDriverWait(driver,600)
group = '"Labs @IITRPR JOC2019"'           #Enter group name within double quotes

x_arg = '//span[contains(@title,'+ group + ')]'
group = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group.click()

header = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[1]/div/span')
header.click()

members = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[1]/div/div/div[1]/span')
members.click()

# TO DO => members list not populating