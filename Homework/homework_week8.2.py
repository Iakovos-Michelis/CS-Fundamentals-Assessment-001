import requests

url = "https://bored.api.lewagon.com/api/activity/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    activity = data['activity']
    print(f"Random activity: {activity}")
else:
    print("Failed to get data from the Bored API.")