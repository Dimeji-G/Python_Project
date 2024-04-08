#================================================Imported Modules=================================
#=======================================Created By Dimzy(Ukwedje Taiwo/Abigail)===================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import random
import string
import time
from selenium.webdriver.chrome.options import Options

#=================================================Variables=======================================
option = Options()
option.add_argument("start-maximized")
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_experimental_option("excludeSwitches", ["enable-automation"])


# Generate a random 4-letter word
random_word = ''.join(random.choices(string.ascii_lowercase, k=4))



#=================================================Main_Code========================================

driver = webdriver.Chrome(options=option)
driver.get("https://email1.io/")
email_raw = driver.find_element(By.CLASS_NAME, 'mailbox-field__input-wrapper')
User_email = (email_raw.text.replace('\n', ''))
user_nameee = User_email.split('@')
user_name = user_nameee[0]
email_inbox_iddd = (driver.current_url).split('=')
email_inbox_id = email_inbox_iddd[1]
email_inbox_link = f'https://email1.io/mailbox/{user_name}?aid={email_inbox_id}'
email_account = f'{user_name}@email1.io'
email_username = f'{user_name[:4]}{random_word}'
email_password = f'{user_name[:4]}1234@#'
print(email_inbox_link)

print(email_username, email_password)
with open('User_Accounts.csv', 'r') as f:
    if f.read()[:8] != 'Username':
        with open('User_Accounts.csv', 'a') as f:
            f.write(f'Username,Password')
            f.write(f'\n{email_username},{email_password}')
    else:
        with open('User_Accounts.csv', 'a') as f:
            f.write(f'\n{email_username},{email_password}')
driver.get('https://www.tiktok.com/signup/phone-or-email/email')
#time.sleep(1)
dropdown_month = driver.find_element(By.CLASS_NAME, 'tiktok-1leicpq-DivSelectLabel')
dropdown_month.click()
random_number_month = random.randint(1,12)
random_number_day = random.randint(1,28)
random_number_year = random.randint(17, 23)
dropdown_month_id = f'Month-options-item-{random_number_month}'
month = driver.find_element(By.ID, dropdown_month_id)
month.click()
dropdown_day = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div[1]')
dropdown_day.click()
dropdown_day_id = f'Day-options-item-{random_number_day}'
day = driver.find_element(By.ID, dropdown_day_id)
day.click()
dropdown_year = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div[1]')
dropdown_year.click()
dropdown_year_id = f'Year-options-item-{random_number_year}'
year = driver.find_element(By.ID, dropdown_year_id)
year.click()
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(email_account)
password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[6]/div/input')
password_field.send_keys(email_password)
#time.sleep(2)
send_code_button = driver.find_element(By.CLASS_NAME, 'tiktok-1jjb4td-ButtonSendCode')
time.sleep(2)
send_code_button.click()
print('Button Clicked.............:)')
try:
    send_code_button.click()
except:
    pass
time.sleep(3)
print(email_inbox_link)
driver2 = webdriver.Chrome(options=option)
driver2.get(email_inbox_link)
time.sleep(3)
email_subject_code = driver2.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div/div[2]/div[3]/div/div/div/table/tbody/tr/td[2]/a/span').text
TT_code = email_subject_code[:6]

print(TT_code)

Verification_Code_Field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[7]/div/div/input')
Verification_Code_Field.send_keys(TT_code)
Next_Submit_Button = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
Next_Submit_Button.click()

time.sleep(3000)
# driver.quit()

