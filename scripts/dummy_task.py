import requests
from datetime import datetime

print("Starting Python automation task...\n")

response = requests.get("https://api.github.com")

print(f"Status Code: {response.status_code}")
print(f"Current Time: {datetime.now()}")

print("\nTask completed successfully.")