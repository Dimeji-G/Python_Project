from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

driver = webdriver.Firefox()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
articlecount = driver.find_element(By.CSS_SELECTOR, '#articlecount a', )
#articlecount.click()

all_portals = driver.find_element(By.LINK_TEXT, 'collapses')
#all_portals.click()

search = driver.find_element(By.NAME,'search')
search.send_keys("Python")
search.send_keys(keys.Keys.ENTER)

#print(articlecount.text)