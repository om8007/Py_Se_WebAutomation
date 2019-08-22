# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:35:56 2019

@author: om8007
"""

from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def loadWebsite():
	#load with result link
	driver.get("http://akuexam.net/RESULTS/")
	#resizing window to get result only screenshot
	driver.set_window_size(620, 1400)
	while driver.title =="Service Unavailable" :
		driver.get("http://akuexam.net/RESULTS/")
		time.sleep(2)     #refreshes every 2 seconds
	#click on 6th sem result link
	wait.until(EC.presence_of_element_located((By.ID ,'ctl00_ContentPlaceHolder1_LinkButton_BTech6thSem_19'))).click()

#creating dir to store captured images
def storageDir():
	cwd=os.getcwd()
	os.makedirs(cwd+'\results',exist_ok=True)
	os.chdir(cwd+'\results')

#fill registration number to check for
def capture():
	reg_input_box = driver.find_element_by_id("ctl00_ContentPlaceHolder1_TextBox_RegNo")
	reg_input_box.send_keys(studs[0])
	show_btn = driver.find_element_by_id("ctl00_ContentPlaceHolder1_Button_Show")
	show_btn.click()

	#saving screenshots and fetching other results
	for reg in studs:
	    #zoom=60% fit the page for full result capture
		driver.execute_script("document.body.style.zoom='60%'")
		file_name = str(reg)+".png"
		driver.get_screenshot_as_file(file_name)
		print("Result captured for {0}".format(str(reg)))
		result_link = driver.current_url
		new_link = result_link.replace(str(reg),str(reg+1))
		driver.get(new_link)

#====# main #====#
driver = webdriver.Chrome(executable_path=r'Z:\python\driver\chromedriver.exe')     #local path to chromedriver
wait = WebDriverWait(driver,20)
#list of registration number whose result to be fetched
studs = [16104107001+x for x in range(40)]

loadWebsite()
storageDir()
capture()

driver.close()

