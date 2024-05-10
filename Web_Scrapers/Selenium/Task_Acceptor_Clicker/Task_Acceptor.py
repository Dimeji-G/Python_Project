#================================================Imported Modules=================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
import time
#===========================================Variables=============================================
email_account = input("Enter your email address: ")
Password = input("Enter your Password: ")
option = Options()
option.add_argument("start-maximized")
#option.add_argument("--headless")
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_argument('log-level=3')
driver = webdriver.Chrome(options=option)
while True:
    try:
        
        #===========================================main_code=============================================
        try:
            driver.get('https://es.smartcat.com')
        except:
            driver = webdriver.Chrome(options=option)
            driver.get('https://es.smartcat.com')            
        Register_Button = driver.find_element(By.XPATH, '//*[@id="headermega"]/div/div/section/div[3]/a[2]')
        Register_Button.click()
        time.sleep(2)
        Email_Field = driver.find_element(By.ID, 'email')
        Email_Field.send_keys(email_account)
        Continue_Button = driver.find_element(By.XPATH, '//*[@id="smartcat"]/div/div/main/div/form/button')
        Continue_Button.click()
        time.sleep(1)
        try:
            Password_Field = driver.find_element(By.ID, 'password')
        except:
            print("Wrong Email Address")
        Password_Field.send_keys(Password)
        signin_button = driver.find_element(By.XPATH, '//*[@id="smartcat"]/div/div/main/form/button')
        signin_button.click()
        time.sleep(5)
        Task_Button = driver.find_element(By.XPATH, '//*[@id="smartcat"]/div/div/main/div/div/div/div/div/a[1]')
        Task_Button.click()
        time.sleep(7)
        project_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/form/table/tbody/tr[1]/td[2]/div/div/div[1]/a')
        invitation_link = f"{project_link.get_attribute('href')}/invitation"
        driver.get(invitation_link)
        time.sleep(5)
        Accept_Button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/invitation-card/div/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button[1]/span')
        Accept_Button.click()
        print('done')
    except Exception as e:
        print(f"Task not available yet")
        driver.quit()
        time.sleep(240)

