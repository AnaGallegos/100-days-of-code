import requests
from datetime import datetime
# # We create a user, only once
username = 'anagagel'
token = '161as2354fsc'
pixela_endpoint = 'https://pixe.la/v1/users'
graphID = 'graph1'


user_params = {
    'token': '161as2354fsc',
    'username': 'anagagel',
    "agreeTermsOfService":"yes", 
    "notMinor":"yes",
}

request_user = requests.post(url = pixela_endpoint, json = user_params)
print(request_user.text)

# Create graphic

pixela_graph = f'{pixela_endpoint}/{username}/graphs'
graph_params = {
    'id' : graphID,
    'name' : 'Reading Tracker',
    'unit' : 'pages',
    'type' : 'int',
    'color' : 'ichou'
}
headers = {
    'X-USER-TOKEN' : token
}

graph1 = requests.post(url = pixela_graph, json= graph_params, headers=headers)

# Create pixel

pixela_graph = f'{pixela_endpoint}/{username}/graphs/{graphID}'

pixel_params = {
    'date': datetime.today().strftime("%Y%m%d"),
    'quantity' : '50',

}
pixel1 = requests.post(url = pixela_graph, json= pixel_params, headers=headers)
print(pixel1.text)