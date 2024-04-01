#================================================Impored Modules================================================
import requests
from datetime import datetime
#================================================Variables======================================================
TOKEN = 'afafasfjafdd23'

time = datetime.now()#datetime(year=2024, month=3, day=11)

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = 'dimzy'

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":'yes',
    'notMinor':'yes',
}

graph_params = {
    'id' : 'graph1',
    'name': 'Self Improving',
    'unit' : 'hour',
    'type':'float',
    'color' :'sora'
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

post_pixel = f'{graph_endpoint}/graph1'

post_pixel_params = {
    'date':time.strftime("%Y%m%d"),
    'quantity':'5.0',
}

#==============================================CODE BODY========================================================

#=============================================registering sticker================================================
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#================================adding sticker===============================================================
response = requests.post(post_pixel, json = post_pixel_params, headers=headers)
print(response.text)

#=================================deleting sticker=============================================================
#response = requests.delete(f'{post_pixel}/{time.strftime("%Y%m%d")}', headers=headers)
#print(response.text)