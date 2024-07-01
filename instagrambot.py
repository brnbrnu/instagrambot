from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the web browser
driver = webdriver.Chrome()

# Open the registration page
driver.get('https://www.instagram.com/')

try:
    # Fill out the registration form
    username_input = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    username_input.send_keys('newwwuser532')

    email_input = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.NAME, 'email'))
    )
    email_input.send_keys('newwuser532@gmail.com')

    password_input = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys('Password123.')

    # Submit the form
    submit_button = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    submit_button.click()

    # Wait for the registration to complete
    WebDriverWait(driver, 120).until(
        EC.url_changes(driver.current_url)
    )

    print("Registration successful!")
    
except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
