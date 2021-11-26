'''
Created on Nov. 25, 2021

@author: 
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from _ast import Assert
from unittest.test import test_assertions
driver = webdriver.Chrome(executable_path="/Users/SGLG/Documents/chromedriver")
driver.get("https://github.com/")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("react")
driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"(//a[@class='f6'])[1]").click()
driver.find_element(By.ID,"search_language").click()
driver.find_element(By.XPATH,"//*[@id='search_language']/optgroup[1]//option[@value='JavaScript']").click()
state = Select(driver.find_element(By.XPATH,"//*[@id='search_state']"))
state.select_by_value("closed")
driver.find_element(By.ID,"search_stars").send_keys(">45")
driver.find_element(By.ID,"search_followers").send_keys(">50")
driver.find_element(By.XPATH,"//*[@id='search_license']/optgroup//option[@value='bsl-1.0']").click()
driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()
result = driver.find_element(By.XPATH,"//div[2]/h3").text
print("=================================================")
print("Number of repositories found:   "+result)
print("One repository found:")
print("1" in result)
print("==================================================")
result = driver.find_element(By.XPATH,"//a[@class='v-align-middle']").text
print("Name of the repository found:  "+result)
print ("Repository Name found:")
print("mvoloskov/decider" in result)
driver.find_element(By.XPATH,"//a[@class='v-align-middle']").click()
readme = driver.find_element(By.XPATH,"//*[@id='readme']/div[3]").text
print("======== FIRST 300 CHARACTERS OF README============")
print(readme[:300])













