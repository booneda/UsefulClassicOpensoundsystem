import requests

response = requests.get('https://randomuser.me/api')

print("Random User Data:\n\n\n\n")

gender = response.json()['results'][0]['gender']
print("Gender: " + (gender))

first_name = response.json()['results'][0]['name']['first']
print("\nFirst Name: " + (first_name))

last_name = response.json()['results'][0]['name']['last']
print("\nLast Name: " + str(last_name))

city = response.json()['results'][0]['location']['city']
print("\nCity: " + str(city))

age = response.json()['results'][0]['dob']['age']
print("\nAge: " + str(age))

dob = response.json()['results'][0]['dob']['date']
print("\nDate of Birth: " + str(dob))
#dob = "Date of Birth"
