from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to display the banner
def display_banner():
    banner = """
     _____        __    __   ____  __            
    |_   _|      / _|   \ \ / /  \/  |           
      | |  _ __ | |_ ___ \ V /| \  / | __ ___  __
      | | | '_ \|  _/ _ \ > < | |\/| |/ _` \ \/ /
     _| |_| | | | || (_) / . \| |  | | (_| |>  < 
    |_____|_| |_|_| \___/_/ \_\_|  |_|\__,_/_/\_\
                                                 
                                                 """
    print(banner)

# Function to display a countdown
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Sleeping for {i} seconds...", end="\r")
        time.sleep(1)

# Display the banner
display_banner()

# Initialize a Selenium web driver with Firefox
driver = webdriver.Firefox()

# Ask the user for a URL
url = input("Enter the URL of the Facebook page: ")

# Load the URL in the web browser
driver.get(url)

# Display a countdown
countdown(10)

# Search for the img tag with the data-imgperflogname attribute set to "profileCoverPhoto"
img_elements = driver.find_elements(By.XPATH, '//img[@data-imgperflogname="profileCoverPhoto"]')

if img_elements:
    # Extract the image URL from the src attribute of the first matching img tag
    img_url = img_elements[0].get_attribute("src")
    
    # Print the image URL
    print(f"Image URL: {img_url}")
else:
    print("Profile is not Public")

# Close the web browser
driver.quit()
