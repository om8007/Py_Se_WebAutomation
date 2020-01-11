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
import time
import csv

driver = webdriver.Firefox(executable_path=r'Z:\python\driver\geckodriver.exe')  #local path to your firefox driver

driver.get("https:/web.whatsapp.com/")
wait = WebDriverWait(driver,600)
group = '"Labs @IITRPR JOC2019"'           #Enter group name within double quotes

x_arg = '//span[contains(@title,'+ group + ')]'
group = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group.click()

header = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[1]/div/span')
header.click()

driver.execute_script("document.body.style.zoom='60%'")

# part = '"participants"'
# participant_arg = '//span[contains(text(),'+ part +')]'
# time.sleep(10)
participant_list = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[1]/div/div/div[1]'))).click()
# wait.until(EC.presence_of_element_located((By.XPATH, x_arg))).click()


participant_box = driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[2]')

# nums=[]
# while 'You' not in nums:
#     link_spans = participant_box.find_elements_by_class_name('_1ovWX')
#     for num in link_spans:
#         number = num.text
#         if number not in nums:
#             nums.append(number)
#     driver.execute_script("arguments[0].scrollBy(0,425);", participant_box)
#     time.sleep(2)
# print(nums)

list = []
for i in range(26):
    divs = participant_box.find_elements_by_class_name('_2WP9Q')
    for div in divs:
        nums = div.find_elements_by_class_name('_1ovWX')
        names = div.find_elements_by_class_name('_3VvbK')
        for num,name in zip(nums, names):
            # i = num.text
            if (num.text,name.text) not in list:
                list.append((num.text,name.text))
    driver.execute_script("arguments[0].scrollBy(0,422);", participant_box)
    time.sleep(2)  
    
driver.refresh()
print(len(list))

with open('group.csv', mode='w+',newline='',encoding="utf-8") as group_file:
    csv_writer = csv.writer(group_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    

    for l in list:
        csv_writer.writerow(l)