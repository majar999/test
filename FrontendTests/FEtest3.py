from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Putanja do ChromeDriver-a
driver_path = r"C:\Tools\chromedriver.exe"
# Putanja do izvršne datoteke Chrome-a
chrome_path = r"C:\Tools\chrome.exe"

# Postavljanje opcija za Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Postavljanje WebDriver-a sa specificiranim Chrome opcijama
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    # Otvaranje web sajta
    driver.get("https://coinmarketcap.com/")

    # Čekanje da kartica Cryptocurrencies bude kliktabilna
    crypto_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/all/views/all/']"))
    )
    crypto_tab.click()

    # Čekanje da opcija Full List bude vidljiva i kliktabilna
    full_list_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Full List')]"))
    )
    full_list_option.click()

    # Snimanje podataka sa trenutne stranice
    # Radi jednostavnosti, ispisujemo naslove top kriptovaluta
    cryptos = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[3]/a"))
    )
    crypto_names = [crypto.text for crypto in cryptos]
    print("Top kriptovalute:")
    for name in crypto_names:
        print(name)

    # Primena bilo koje kombinacije filtera (ovo zavisi od dostupnih filtera na sajtu)
    # Na primer, primena filtera za kriptovalute sa visokim tržišnim kapitalom
    filter_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Filters')]"))
    )
    filter_button.click()

    # Primer filtera: Tržišni kapital > $1B
    market_cap_filter = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '> $1B')]"))
    )
    market_cap_filter.click()

    # Primena filtera
    apply_filter_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
    )
    apply_filter_button.click()

    # Provera podataka u odnosu na podatke snimljene u koraku 4
    # Radi jednostavnosti, ispisujemo naslove filtriranih kriptovaluta
    filtered_cryptos = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[3]/a"))
    )
    filtered_crypto_names = [crypto.text for crypto in filtered_cryptos]
    print("Filtrirane kriptovalute:")
    for name in filtered_crypto_names:
        print(name)

finally:
    # Zatvaranje WebDriver-a
    driver.quit()
