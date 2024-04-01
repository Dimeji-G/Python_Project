#================================================Imported Modules=================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
#===================================================Main_Code=====================================
driver = webdriver.Firefox()
driver.get('http://secure-retreat-92358.herokuapp.com')
fname = driver.find_element(By.NAME, 'fName')
fname.send_keys('Dimzy')
lname = driver.find_element(By.NAME, 'lName')
lname.send_keys("The next Big Thing")
email = driver.find_element(By.NAME, 'email')
email.send_keys('Ukwedjedimej@gmail.com')

button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()