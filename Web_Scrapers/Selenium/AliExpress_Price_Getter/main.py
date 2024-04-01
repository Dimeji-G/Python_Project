#=============================================Imported_Modules=================================================
from selenium import webdriver
from selenium.webdriver.common.by import By

#==============================================Variables========================================================
#firefox_driver_path = 'geckodriver'
driver = webdriver.Firefox()
driver.get('https://www.aliexpress.com/item/1005006364535458.html?spm=a2g0o.best.moretolove.19.33412c25KGJZwf')
#price = driver.find_elements(By.CLASS_NAME, 'es--char53--VKKip5c')
get_price = driver.find_element(By.CSS_SELECTOR, 'div.es--wrap--erdmPRe')
price = (get_price.text)
price_num = price[3:]
init_price = (price_num.replace(',', ''))
med_price = (init_price.split('.'))
final_price = int(med_price[0])
print(final_price)

# but_link = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/dl/dd/a[13]').get_attribute('href')
# print(but_link)
driver.quit()