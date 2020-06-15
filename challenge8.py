from webexteamssdk import WebexTeamsAPI
import requests
import json


webex_api = "https://webexapis.com/v1"
bot_access_token = 'Yzc1MGM1ZjUtNzBlZS00OTk3LWFiMGMtZDIzNDFkN2Q4NTM2MDRjYTJhMmYtNGM4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

def clean_up():
    url = webex_api + '/rooms'

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + bot_access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    for data in response.json()['items']:
        url = webex_api + '/rooms/' + data['id']
        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

def create_room():
    url = webex_api + '/rooms'

    headers = {
        'Authorization': 'Bearer ' + bot_access_token
    }
    payload = {
    'title': 'Oneal-Stewart-DevNet-Test'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

def add_membership():
    url = webex_api + '/rooms'

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + bot_access_token
    }

    response1 = requests.request("GET", url, headers=headers, data=payload)
    print(response1.text.encode('utf8'))

    # Get roomId to add membership to room
    for data1 in response1.json()["items"]:
        room_id = data1['id']
        url = webex_api + '/memberships/'
        payload = {
            'roomId': room_id,
            'personEmail': 'onstewar@cisco.com'
        }
        response2 = requests.request("POST", url, headers=headers, data=payload)

        print(response2.text.encode('utf8'))

        # Welcome message to member added to the room
        url = webex_api + '/messages/'
        payload = {
            'roomId': room_id,
            'text': 'Hello, Welcome to CSA - DevNet Study Group Challenge #8 Test space.'
        }
        response3 = requests.request("POST", url, headers=headers, data=payload)
        print(response3.text.encode('utf8'))

# Call functions
clean_up()
create_room()
add_membership()



