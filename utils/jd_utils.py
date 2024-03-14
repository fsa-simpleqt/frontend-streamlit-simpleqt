import requests
import json
import re


url = "https://your-server-url/api/get_all_jds"

  
response = requests.get(url, headers={"Content-Type": "application/json"})

if response.status_code == 200:
        data = response.json()
else:
        print(f"Lỗi truy cập dữ liệu: {response.status_code}")

