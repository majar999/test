from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
driver_path = r"C:\Tools\chromedriver.exe"
# Path to Chrome executable
chrome_path = r"C:\Tools\chrome.exe"

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Set up the WebDriver with the specified Chrome options
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    # Open the website
    driver.get("https://coinmarketcap.com/")

    # Wait for the Cryptocurrencies tab to be clickable
    crypto_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/all/views/all/']"))
    )
    crypto_tab.click()

    # Wait for the Full List option to be visible and click it
    full_list_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Full List')]"))
    )
    full_list_option.click()

    # Record the data on the current page
    # For simplicity, we'll just print the titles of the top cryptocurrencies
    cryptos = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[3]/a"))
    )
    crypto_names = [crypto.text for crypto in cryptos]
    print("Top Cryptocurrencies:")
    for name in crypto_names:
        print(name)

    # Apply any combination of filters (this will depend on the available filters on the site)
    # For example, applying a filter for cryptocurrencies with high market cap
    filter_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Filters')]"))
    )
    filter_button.click()

    # Example filter: Market Cap > $1B
    market_cap_filter = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '> $1B')]"))
    )
    market_cap_filter.click()

    # Apply the filter
    apply_filter_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
    )
    apply_filter_button.click()

    # Check against the data recorded in Step 4
    # For simplicity, we'll just print the titles of the filtered cryptocurrencies
    filtered_cryptos = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[3]/a"))
    )
    filtered_crypto_names = [crypto.text for crypto in filtered_cryptos]
    print("Filtered Cryptocurrencies:")
    for name in filtered_crypto_names:
        print(name)

finally:
    # Close the WebDriver
    driver.quit()
