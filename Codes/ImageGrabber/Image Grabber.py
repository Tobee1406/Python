#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_images(url):
    # Send a request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Extract the src attribute from each img tag
    img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]
    
    return img_urls

# Get the URL of the site you want to scrape from the user
website_url = input('Enter the URL of the website: ')

# Get all images from the website
images = get_all_images(website_url)

# Print the found images
print("Found images:")
for img in images:
    print(img)
