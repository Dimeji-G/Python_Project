#=============================================Imported_Modules=================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#==============================================Variables========================================================
driver = webdriver.Firefox()

#===================================Main_Code======================================================================
driver = webdriver.Firefox()
driver.get('https://www.python.org')

# Scrape data
time_event = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
Event_Name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = []

for x in range(len(time_event)):
    events.append({
        'time': time_event[x].text,
        'name': Event_Name[x].text
    })

# Create DataFrame
df = pd.DataFrame(events)

# Export to Excel
df.to_excel('events.xlsx', index=False)

# Quit WebDriver
driver.quit()
