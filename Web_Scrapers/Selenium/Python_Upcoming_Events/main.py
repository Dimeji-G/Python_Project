#=============================================Imported_Modules=================================================
from selenium import webdriver
from selenium.webdriver.common.by import By

#==============================================Variables========================================================
driver = webdriver.Firefox()

#===================================Main_Code======================================================================
driver.get('https://www.python.org')
# #Upcomiing Events
# first_time = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# first_name = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')

# second_time = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time')
# second_name = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a')

# third_time = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/time')
# third_name = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/a')

# fourth_time = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/time')
# fourth_name = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/a')

# fifth_time = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/time')
# fifth_name = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/a')



# Upcoming_Event_Dict = {
#     '0' : {
#         'time' : first_time.text,
#         'name' : first_name.text
#     },
    
#     '1' : {
#         'time' : second_time.text,
#         'name' : second_name.text,         
#     },
    
#     '2' : {
#         'time': third_time.text,
#         'name': third_name.text,
#     },
    
#     '3' : {
#         'time' : fourth_time.text,
#         'name' : fourth_name.text,        
#     },    
    
#     '4' : {
#         'time' : fifth_time.text,
#         'name' : fifth_name.text
#     },
# }

# print(Upcoming_Event_Dict)

time_event = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
Event_Name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for x in range((len(time_event))):
    events[x] = {
        'time' : time_event[x].text,
        'name' : Event_Name[x].text
}

print(events)

driver.quit()