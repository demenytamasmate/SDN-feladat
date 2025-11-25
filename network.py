import requests

api_url = "http://192.168.101.254/api/v1/network-device"


service_ticket = "3f3da0ee45d84a2ea4e45a2cd38b0a13"

headers = {
    "X-Auth-Token": service_ticket
}

response = requests.get(api_url, headers=headers)

print("Request status:", response.status_code)

try:
    devices = response.json()["response"]

    for device in devices:
        hostname = device.get("hostname")
        platform = device.get("platformId")
        mgmt_ip = device.get("managementIpAddress")
        print(f"{hostname}\t{platform}\t{mgmt_ip}")

except Exception as e:
    print("Hiba történt JSON feldolgozás közben:")
    print(response.text)
    print(e)
