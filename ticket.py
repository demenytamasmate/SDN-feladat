import requests
import json

api_url = "http://192.168.101.254/api/v1/ticket"

payload = {
    "username": "admin",
    "password": "admin123"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(api_url, data=json.dumps(payload), headers=headers)

print("Ticket request status:", response.status_code)

try:
    data = response.json()
    print("Service ticket:", data["response"]["serviceTicket"])
except:
    print("Raw response:", response.text)
