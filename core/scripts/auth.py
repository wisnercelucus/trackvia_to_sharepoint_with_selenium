import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login_to_trackvia(driver=None, login_url=None, username=None, password=None):
    try:
        # Open the TrackVia login page
        driver.get(login_url)
        time.sleep(3)  # Wait for the page to load
    
        # Find and fill in the username field
        username_field = driver.find_element(By.ID, "sign-in-page__email")
        username_field.send_keys(username)
    
        # Find and fill in the password field
        password_field = driver.find_element(By.ID, "sign-in-page__password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    
        time.sleep(5)
    
        print("Login successful.")
    
    except Exception as e:
        print(f"Error: {e}")