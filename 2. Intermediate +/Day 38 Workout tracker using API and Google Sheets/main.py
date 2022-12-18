import requests
from datetime import datetime


APP_ID = 'YOUR ID'
API_KEY = 'YOUR API'

GENDER = 'FEMALE'
WEIGHT_KG = '70'
HEIGHT_CM = '179'
AGE = 27




exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = 'https://api.sheety.co/7d9ca34a36c3f344254d242a733503b7/copiaDeMyWorkouts/workouts'

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()['exercises']

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X"),
for exercise in result: 
    sheety_params = {
        'workout' : {
            'Date': date,
            'Time': time,
            'exercise': exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"]
            }
        }
sheet_response = requests.post(sheety_endpoint, json=sheety_params)

print(sheet_response.text)