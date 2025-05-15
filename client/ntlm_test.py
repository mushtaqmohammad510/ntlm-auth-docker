import requests
from requests_ntlm import HttpNtlmAuth

apache_host = "apache-server"

try:
    response = requests.get(
        f"http://{apache_host}/protected",
        auth=HttpNtlmAuth('testuser', 'password')
    )
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except Exception as e:
    print("Connection failed:", str(e))
