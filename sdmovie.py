from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

name = input("Enter movie name : ")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://1sdmoviespoint.com/')

sleep(2)

searchBox = driver.find_element_by_xpath('//*[@id="search-live-field-196880072"]')
searchBox.send_keys(name)
sleep(2)
searchBox.send_keys(Keys.RETURN)

