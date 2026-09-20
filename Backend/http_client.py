import json
from urllib.request import Request, urlopen


data = {
    "message": "What is an API?",
}

json_data = json.dumps(data).encode()

request = Request(
    "http://localhost:8000/chat",
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

response = urlopen(request)

response_data = response.read().decode()

print(response_data)