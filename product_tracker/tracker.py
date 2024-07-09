from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Path to the Brave browser executable
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"  # Adjust this path as necessary

# Configure options for Brave
options = Options()
options.binary_location = brave_path
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Specify the path to your ChromeDriver
chromedriver_path = "/usr/local/bin/chromedriver"  # Adjust this path as necessary

service = BraveService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL of the Zara product
zara_url = 'https://www.zara.com/za/en/textured-split-suede-running-sneakers-p12323320.html?v1=310995825&v2=2037252&page=5'

# Fetch the page
driver.get(zara_url)

# Parse the rendered HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract the price (adjust the CSS selector based on the actual page structure)
price_tag = soup.find('span', {'class': 'price-tag'})
if price_tag:
    price_text = price_tag.get_text(strip=True).replace('R', '').replace(',', '')
    price = float(price_text)
    print(f"The price of the item is: R{price}")
else:
    print("Price not found")

# Close the browser
driver.quit()
