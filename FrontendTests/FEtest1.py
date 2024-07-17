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
            print("Pokušavam da kliknem dugme All")
            all_button_selector = "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-d577b7d4-4.dZhWhQ > div.sc-4c05d6ef-0.sc-c652d51c-1.sc-6fa8c3d4-0.dlQYLv.jOvctx.eDTcwB.table-control-outer-wrapper.scroll-indicator.scroll-initial.hideArrow > div.scroll-child > div.sc-4c05d6ef-0.FfYmA.table-link-area > a:nth-child(1) > button"
            all_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, all_button_selector))
            )
            self.driver.execute_script("arguments[0].click();", all_button)
            print("Dugme All je uspešno kliknuto.")
        except Exception as e:
            print(f"Greška prilikom klikanja na dugme All: {e}")
            self.driver.quit()

    def verify_all_results_displayed(self):
        """
        Verifikacija da su svi rezultati prikazani posle pritiska na dugme 'All'.
        """
        try:
            print("Verifikacija da su svi rezultati prikazani.")
            table_selector = "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"
            table = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, table_selector))
            )
            rows = table.find_elements(By.TAG_NAME, "tr")
            print(f"Broj pronađenih rezultata: {len(rows)}")
            return len(rows) > 0
        except Exception as e:
            print(f"Greska prilikom verifikacije: {e}")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            return False

    def run_test(self):
        """
        Pokrećemo test koji otvara web stranicu, klikne dugme All i verifikuje rezultate.
        """
        print("Početak testa.")
        self.open_coinmarketcap()
        self.click_all()
        if self.verify_all_results_displayed():
            print("Test je prošao: Svi rezultati su prikazani.")
        else:
            print("Test je pao: Nema prikazanih rezultata.")
        self.driver.quit()
        print("Test je završen.")

if __name__ == "__main__":
    driver_path = "C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver.exe"
    chrome_path = "C:\\Users\\Administrator\\Downloads\\chrome-win64\\chrome-win64\\chrome.exe"
    test = CoinMarketCapTest(driver_path, chrome_path)
    test.run_test()
