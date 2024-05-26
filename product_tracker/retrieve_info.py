# import requests
# from bs4 import BeautifulSoup
# import time

# def get_zara_product_details(url):
#   """
#   Attempts to extract product details from a Zara URL using web scraping.

#   Args:
#       url: The URL of the Zara product page.

#   Returns:
#       A dictionary containing extracted product details (title, price, etc.), 
#       or None if unsuccessful.

#   Raises:
#       Exception: If an unexpected error occurs during scraping.
#   """

#   try:
#     # Respect robots.txt and avoid overloading server (adjust delay as needed)
#     time.sleep(2)

#     response = requests.get(url)
#     response.raise_for_status()  # Raise exception for non-200 status codes

#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Identify elements containing details (adapt selectors for Zara's website)
#     title_element = soup.find("h1", class_="product-detail__name")
#     price_element = soup.find("span", class_="price__SAR")

#     if title_element and price_element:
#       return {
#           "title": title_element.text.strip(),
#           "price": float(price_element.text.strip().replace("SAR ", "")),
#       }
#     else:
#       print(f"Failed to extract details for {url}. Website structure might have changed.")
#       return None

#   except requests.exceptions.RequestException as e:
#     print(f"Error fetching product details: {e}")
#     return None
#   except Exception as e:
#     print(f"Unexpected error: {e}")
#     raise e  # Re-raise for handling in the calling code

# # Example usage (replace with a Zara product URL)
# product_url = "https://www.zara.com/za/en/textured-split-suede-running-sneakers-p12323320.html?v1=310995825&v2=2037252"
# product_details = get_zara_product_details(product_url)

# if product_details:
#   print(f"Product Title: {product_details['title']}")
#   print(f"Price: SAR {product_details['price']:.2f}")
# else:
#   print("Failed to retrieve product details.")


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