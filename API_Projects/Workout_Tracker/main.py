#========================================================Imported_Modules======================================
import requests
from datetime import datetime

#=====================================================Variables================================================
APP_ID = 'c313a2e2'
API_KEY = '73ffb3114b22e520f5b50792e3a45ee5'
Sheety_KEY = 'DimzyBOY'
exercise_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
food_endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

TIME = datetime.now()

SheetyEndpoint = 'https://api.sheety.co/734820dfc587707330344e6d02c4698e/dimzyWorkout/sheet1'

InputQuestion = input('Exercise or food: ' )

exercise_headers = {
    'x-app-id':APP_ID,
    'x-app-key': API_KEY,
}

sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {Sheety_KEY}'
}


#===================================================Main_Code==================================================

#=============================================Exercise_API__Calories_Calculator================================
if InputQuestion.title() == 'Exercise':
    INPUTexercise = input("Enter your exercise deed: ")

    # INPUTage = input("Enter your age in years: ")

    # INPUTweight = input("Enter your weight in kg: ")

    # INPUTheight = input("Enter your height in cm: ")

    Exercise_params = {
        'query':INPUTexercise,
        # 'weight_kg': INPUTweight,
        # 'height_cm': INPUTheight,
        # 'age': INPUTage,
    }
    
    
    data = requests.post(exercise_ENDPOINT, json=Exercise_params, headers=exercise_headers)
    response = data.json()
    
    for exercise in response['exercises']:        
        sheety_Params = {
            "sheet1" : {
                "date": TIME.strftime('%x'),
                "time": TIME.strftime('%X'),
                "exercise": exercise['name'],
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories'],
            }
        }
        
    sheety_response = requests.post(SheetyEndpoint, json=sheety_Params, headers=sheety_headers)
    print(sheety_response.text)
    

#=============================================Food API Calories Calculator=====================================
else:
    INPUTfood = input("Enter what you ate: ")
    
    food_params = {
        'query':INPUTfood,
    }
    
    response = requests.post(food_endpoint, json=food_params, headers=exercise_headers)
    print(response.json())