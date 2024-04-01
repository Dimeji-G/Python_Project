#======================================================================Imported Modules=============================================================================#
import requests
from bs4 import BeautifulSoup

#======================================================================variable=====================================================================================
#info = input('Enter the date, year and time in this format (yyyy-mm-dd): ')
date = '2023-11-29'
LINK = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(LINK)
content = response.text
#=======================================================================Main Code ===================================================================================#

if response.status_code == 200:
    soup = BeautifulSoup(content, 'html.parser')
    songs = soup.select('div ul li h3')
    result = '\n'.join(song.get_text(strip=True) for song in songs)
    
    with open('billboard.txt', 'a') as f:
        f.write(result)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
