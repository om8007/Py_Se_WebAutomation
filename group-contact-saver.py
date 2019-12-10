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
group = '" <target group name as in your whatsapp> "'           #Enter group name within double quotes

x_arg = '//span[contains(@title,'+ group + ')]'
group = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group.click()

three_dots_arg='//*[@id="main"]/header/div[3]/div/div[3]/div/span'
dot_menu = wait.until(EC.presence_of_element_located((By.XPATH, three_dots_arg)))
dot_menu.click()

group_info_arg = '//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[1]/div'
group_info = wait.until(EC.presence_of_element_located((By.XPATH, group_info_arg)))
group_info.click()

members_arg = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[1]/div/div/div[1]/span'
members_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,members_arg)))
members_list.click()

