import requests
import json

API_URL = "https://your-api-endpoint.com/api/v1/ticket"
USERNAME = "admin"
PASSWORD = "password"

def get_service_ticket():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(API_URL, json=payload, verify=False)
    
    if response.status_code != 200:
        raise Exception(f"Hiba a ticket lekérésekor: {response.status_code} - {response.text}")

    ticket = response.json().get("serviceTicket")
    print("Service ticket:", ticket)
    return ticket

if __name__ == "__main__":
    get_service_ticket()
