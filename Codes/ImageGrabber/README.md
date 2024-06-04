# Image Grabber

## Guide
### Setup
Install Beautifulsoup4:

```pip install requests beautifulsoup4```

### Step 1:
Run the code.

### Step 2:
Paste the URL in the terminal and press enter.


## Code explanation
### 1. Import Libraries:

- ```requests```: To send HTTP requests to the website.
- ```BeautifulSoup``` from bs4: To parse the HTML content of the web page.
- ```urljoin``` from ```urllib.parse```: To handle relative URLs correctly.

### 2. Function Definition:

- ```get_all_images(url)```: This function takes a URL as an input and returns a list of all image URLs found on that page.

### 3. Sending Request:

- ```requests.get(url)```: Sends a GET request to the provided URL.

### 4. Check for Successful Request:

- Checks if the status code of the response is 200 (HTTP OK).

### 5. Parsing HTML Content:

- ```BeautifulSoup(response.content, 'html.parser')```: Parses the HTML content using BeautifulSoup.

### 6. Finding Image Tags:

- ```soup.find_all('img')```: Finds all img tags in the HTML.

### 7. Extracting Image URLs:

- ```img['src']```: Extracts the src attribute of each img tag.
- ```urljoin(url, img['src'])```: Ensures that the image URLs are absolute URLs.

### 8. Result:

- Prints the list of image URLs found on the website.

### Note:
- Ensure you have permission to scrape the website. Scraping websites without permission can be against their terms of service.
- For more advanced web scraping, consider handling pagination, downloading images, and adding error handling and logging.
