from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://kissa47.blogspot.com/2025/06/%20.html"

options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize browser
driver = webdriver.Chrome(options=options)

# Simulate views
for i in range(10):  # You can change 10 to 1000
    try:
        driver.get(url)
        print(f"View {i+1} loaded")
        time.sleep(10)  # Simulate reading time
    except Exception as e:
        print(f"Error at view {i+1}: {e}")

driver.quit()
