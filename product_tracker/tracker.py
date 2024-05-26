# import requests
# from bs4 import BeautifulSoup
# import smtplib  # for email notifications (optional)

# def check_stock(url, sender_email=None, receiver_email=None):
#   """
#   Checks product stock and price on a website and sends notification for changes.

#   Args:
#       url: The URL of the product page.
#       sender_email (optional): Email address for sending notifications.
#       receiver_email (optional): Email address to receive notifications.
#   """
#   try:
#     # Fetch product page content
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract price and availability text (adjust selectors for specific website)
#     price_element = soup.find("span", class_="price")
#     availability_element = soup.find("div", class_="stock-status")

#     # Process and store extracted information
#     current_price = None
#     in_stock = False
#     if price_element:
#       current_price = float(price_element.text.strip().replace("$", ""))
#     if availability_element:
#       in_stock_text = availability_element.text.strip().lower()
#       in_stock = "in stock" in in_stock_text or "available" in in_stock_text

#     # Load previous data from a file (implement logic for file handling)
#     previous_data = load_previous_data(url)
#     previous_price = previous_data.get("price")
#     previous_stock = previous_data.get("in_stock", False)

#     # Check for changes and send notifications
#     if current_price and (current_price != previous_price):
#       send_notification(f"Price drop for {url}! New price: ${current_price:.2f}", sender_email, receiver_email)
#     if in_stock and not previous_stock:
#       send_notification(f"Back in stock! {url}", sender_email, receiver_email)

#     # Update previous data for future comparisons
#     save_previous_data(url, {"price": current_price, "in_stock": in_stock})

#   except Exception as e:
#     print(f"Error checking product: {url} - {e}")

# def send_notification(message, sender_email, receiver_email):
#   """
#   Sends an email notification for stock or price changes (optional).

#   Args:
#       message: The notification message to send.
#       sender_email: Email address for sending notifications.
#       receiver_email: Email address to receive notifications.
#   """
#   if sender_email and receiver_email:
#     # Configure SMTP server details (replace with your email provider settings)
#     smtp_server = "smtp.your_email_provider.com"
#     port = 587  # or 465 for SSL

#     with smtplib.SMTP(smtp_server, port) as server:
#       server.starttls()
#       server.login(sender_email, "your_email_password")
#       server.sendmail(sender_email, receiver_email, message)
#       print(f"Notification sent for {url}")

# def load_previous_data(url):
#   """
#   Loads previously stored data for the product URL (implement file I/O).

#   Args:
#       url: The URL of the product page.

#   Returns:
#       A dictionary containing previously stored information (price, stock).
#   """
#   # Replace with your implementation to load data from a file based on URL
#   return {}

# def save_previous_data(url, data):
#   """
#   Saves current data for future comparisons (implement file I/O).

#   Args:
#       url: The URL of the product page.
#       data: A dictionary containing price and stock information.
#   """
#   # Replace with your implementation to save data to a file based on URL
#   with open("Retrieved_data.txt", "a+", newline='') as file:
#     retrieved = file.write(data)

# # Example usage (replace with your email addresses if using notifications)
# product_url = "https://www.zara.com/za/en/textured-split-suede-running-sneakers-p12323320.html?v1=310995825&v2=2037252"
# # sender_email = "your_email@example.com"  # uncomment for email notifications
# # receiver_email = "recipient_email@example.com"  # uncomment for email notifications
# check_stock(product_url)



import requests
from bs4 import BeautifulSoup

def get_product_info(url):
    # Send a request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the product name
    product_name = soup.find('h1', {'class': 'product-name'}).text.strip()

    # Find the price
    price_element = soup.find('span', {'class': 'price'})
    if price_element:
        price = price_element.text.strip()
    else:
        price = 'N/A'

    # Find the availability status
    availability_element = soup.find('p', {'class': 'availability'})
    if availability_element:
        availability = availability_element.text.strip()
    else:
        availability = 'N/A'

    return product_name, price, availability

# Example usage
url = 'https://www.zara.com/us/en/share/-p05242308.html'
product_name, price, availability = get_product_info(url)

print(f'Product: {product_name}')
print(f'Price: {price}')
print(f'Availability: {availability}')