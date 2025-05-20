import requests
from requests_ntlm import HttpNtlmAuth

url = "http://ntlm-apache"  # Using service name as hostname

try:
    response = requests.get(
        url,
        auth=HttpNtlmAuth('testuser', 'password')
    )
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except Exception as e:
    print("Connection failed:", str(e))
