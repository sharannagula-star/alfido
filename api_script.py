import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()

    users = response.json()

    search_city = input("Enter city name: ")

    found = False

    for user in users:
        if user["address"]["city"].lower() == search_city.lower():
            print("\nUser Found:")
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            found = True

    if not found:
        print("No users found in that city.")

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)
except requests.exceptions.ConnectionError:
    print("Connection Error. Check internet connection.")
except requests.exceptions.Timeout:
    print("Request Timed Out.")
except requests.exceptions.RequestException as e:
    print("Error:", e)
