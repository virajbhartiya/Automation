from selenium import webdriver
from time import sleep
"""
name = input("Enter song name : ")

driver = webdriver.Chrome("C:\\Users\\vlbha\\Desktop\\Code\\Python\\Automation\\chromedriver.exe")
driver.maximize_window()
driver.get('https://mp3paw.com')

searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys(name)

searchButtion = driver.find_element_by_xpath('//*[@id="submit"]/span')
searchButtion.click()

download = driver.find_element_by_xpath('//*[@id="mp3List"]/div[1]/div[3]/ul/li[3]/div')
download.click()

sleep(10)

link = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/ul/li[1]")
sleep(2)
link.click()


"""
name = input("Enter song name : ")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mp3quack.com')

searchBox = driver.find_element_by_xpath('//*[@id="searchInput"]')
searchBox.send_keys(name)

searchButtion = driver.find_element_by_xpath('//*[@id="searchSubmit"]/span')
searchButtion.click()

download = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/ul/li[3]')
download.click()

