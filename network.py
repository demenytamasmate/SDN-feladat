import requests
import json

TICKET = "IDE_TEDD_BE_A_TICKETET"  # vagy importáld a ticket.py-ból
API_URL = "https://your-api-endpoint.com/api/v1/network/devices"

def list_devices():
    headers = {
        "X-Auth-Token": TICKET,
        "Content-Type": "application/json"
    }

    response = requests.get(API_URL, headers=headers, verify=False)

    if response.status_code != 200:
        raise Exception(f"Hiba az eszközök lekérésekor: {response.status_code} - {response.text}")

    devices = response.json().get("devices", [])

    for dev in devices:
        platform = dev.get("platformId", "N/A")
        ip_addr = dev.get("managementIpAddress", "N/A")
        print(f"Platform: {platform}   |   Management IP: {ip_addr}")

if __name__ == "__main__":
    list_devices()
