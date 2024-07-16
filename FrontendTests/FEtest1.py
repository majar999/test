from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoinMarketCapTest:
    """
    Klasa za testiranje funkcionalnosti CoinMarketCap veb stranice koristeći Selenium WebDriver.
    """

    def __init__(self, driver_path, chrome_path):
        """
        Inicijalizuje WebDriver.
        
        :param driver_path: Putanja do WebDriver izvršnog fajla.
        :param chrome_path: Putanja do Chrome izvršnog fajla.
        """
        chrome_options = Options()
        chrome_options.binary_location = chrome_path
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
        chrome_options.add_argument("--disable-extensions")  # Disable extensions
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.maximize_window()
        print("WebDriver uspešno inicijalizovan.")

    def open_coinmarketcap(self):
        """
        Otvara CoinMarketCap veb stranicu.
        """
        try:
            print("Otvaranje CoinMarketCap veb stranice.")
            self.driver.get("https://coinmarketcap.com")
            print("Web stranica uspešno otvorena.")
        except Exception as e:
            print(f"Došlo je do greške prilikom otvaranja veb stranice: {e}")

    def click_all(self):
        """
        Kliknuti 'All' dugme za prikaz svih rezultata.
        """
        try:
            print("Pokusavam da kliknem dugme All")
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            all_button = next(button for button in buttons if button.text.strip() == 'All')
            self.driver.execute_script("arguments[0].click();", all_button)
            print("Dugme All je uspesno kliknuto.")
        except Exception as e:
            print(f"Greska prilikom klikanja na dugme All: {e}")
            self.driver.quit()

    def verify_all_results_displayed(self):
        """
        Verifikacija da su svi rezultati prikazani posle pritiska na dugme 'All'.
        """
        try:
            print(" Verifikacija da su svi rezultati prikazani.")
            results = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "cmc-table-row"))
            )
            print(f"Broj pronadjenih rezultata: {len(results)}")
            return len(results) > 0
        except Exception as e:
            print(f"Greska prilikom verifikacije: {e}")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            return False

    def run_test(self):
        """
        Pokrecemo test koji otvara web stranicu klikne dugme All i verifikuje rezultate.
        """
        print("Pocetak testa.")
        self.open_coinmarketcap()
        self.click_all()
        if self.verify_all_results_displayed():
            print("Test je prosao: Svi rezultati su prikazani.")
        else:
            print("Test je pao: Nema prikazanih rezultata.")
        self.driver.quit()
        print("Test je zavrsen.")

if __name__ == "__main__":
    driver_path = "C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver.exe"
    chrome_path = "C:\\Users\\Administrator\\Downloads\\chrome-win64\\chrome-win64\\chrome.exe"
    test = CoinMarketCapTest(driver_path, chrome_path)
    test.run_test()
