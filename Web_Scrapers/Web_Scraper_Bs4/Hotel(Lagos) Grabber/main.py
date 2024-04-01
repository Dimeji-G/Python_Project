#=================================================Imported Modules=============================================
from bs4 import BeautifulSoup
import requests
import math

#=================================================Variables====================================================
try:
    requested_location = input('Enter any Lagos city or Local Gov to view all the Hotels there: ').lower()
    hotel_url_for_getting_total_number = f'https://hotels.ng/hotels-in-lagos/{requested_location}'
    excel_sheet_endpoint = 'https://api.sheety.co/734820dfc587707330344e6d02c4698e/hotelGrabber/sheet1'
    authorization_token = 'DimzyBOY'
    excel_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {authorization_token}'
    }
    Hotel_names = []
    Hotel_Location = []
    Hotel_Link = []
    #==================================================Main Code==================================================    
    page = requests.get(hotel_url_for_getting_total_number)
    soup = BeautifulSoup(page.content, 'html.parser')
    Hotel_Number = soup.find(class_='total_results').get_text(strip=True)
    hotel_range = math.floor(int(Hotel_Number) / 10)
    if hotel_range % 10 != 0:
        total_hotel_pages = hotel_range + 1
        loopable_hotel_number = total_hotel_pages + 1
        print(f'There are a total of {Hotel_Number} registered Hotels in {requested_location.title()}')

    for x in range(1, loopable_hotel_number):
        hotel_url = f'{hotel_url_for_getting_total_number}/{x}'
        page = requests.get(hotel_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        Hotel_Listing_Names = soup.find_all(class_='listing-hotels-name')
        Hotel_Listing_Location = soup.find_all(class_="listing-hotels-address color-dark hidden-md hidden-lg")
        Hotel_Listing_Link = soup.select('.col-xs-4 a')
        
        for name in Hotel_Listing_Names:
            Hotel_names.append(name.get_text(strip=True))
        
        for location in Hotel_Listing_Location:
            Hotel_Location.append(location.get_text(strip=True))
            
        for link in Hotel_Listing_Link:
            Hotel_Link.append(link.get('href'))
            


    #the enumerate tell it to start from 0
    #the zip tells it to  pair it and iterate through them both
    #this line iterates over the hotel names and locations,\
        # prints them with a corresponding number \
            # (starting from 1), and does this for all\
                # hotels in the lists 
    for number, (name, location, link) in enumerate(zip(Hotel_names, Hotel_Location, Hotel_Link), start=1):
        print(f'{number} {name} {location}, {link}')
        

    #==========================================API KEY CALL=======================================================
        sheety_Params = {
        "sheet1" : {
            "name": f'{name}',
            "location": f'{location}',
            "link": f'{link}',
            }
        }
        
        sheety_response = requests.post(excel_sheet_endpoint, json=sheety_Params, headers=excel_headers) 
    print(sheety_response.text)
except:
    print("City doesn't exist or you must have mispelt your city name, try again")