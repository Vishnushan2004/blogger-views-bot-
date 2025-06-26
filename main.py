import requests
import time

url = "https://kissa47.blogspot.com/2025/06/%20.html"  # replace with your URL
views = 1000

for i in range(views):
    try:
        res = requests.get(url)
        print(f"[{i+1}] Status: {res.status_code}")
        time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")
