from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

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
        # Postavljanje opcija za Chrome
        chrome_options = Options()
        chrome_options.binary_location = chrome_path
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--no-sandbox")  # Onemogućava sandbox
        chrome_options.add_argument("--disable-extensions")  # Onemogućava ekstenzije
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
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"))
            )
            print("Veb stranica uspešno otvorena.")
        except Exception as e:
            print(f"Došlo je do greške prilikom otvaranja veb stranice: {e}")

    def add_to_watchlist(self, num_to_add):
        """
        Biranje nasumičnih kriptovaluta i dodavanje na watchlist.
        """
        try:
            print(f"Biranje {num_to_add} nasumičnih kriptovaluta za dodavanje na watchlist.")
            table = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"))
            )
            crypto_rows = table.find_elements(By.TAG_NAME, "tr")
            selected_indices = random.sample(range(len(crypto_rows)), num_to_add)
            for index in selected_indices:
                add_to_watchlist_selector = "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table > tbody > tr:nth-child(3) > td:nth-child(1) > span > span"
                add_to_watchlist = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, add_to_watchlist_selector))
                )
                self.driver.execute_script("arguments[0].scrollIntoView();", add_to_watchlist)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of(add_to_watchlist)
                )
                self.driver.execute_script("arguments[0].click();", add_to_watchlist)
                time.sleep(2)  # Kratko kašnjenje kako bi se osiguralo da je stavka dodata
                
                # Zatvaranje popup prozora
                close_popup_selector = "body > div.sc-acb6320-0.jPvGvf.modalOpened > div > div > div > svg"
                close_popup = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, close_popup_selector))
                )
                close_popup.click()
                time.sleep(1)  # Kratko kašnjenje kako bi se osiguralo da je popup zatvoren
                
            print(f"{num_to_add} kriptovaluta dodata na watchlist.")
        except Exception as e:
            print(f"Došlo je do greške prilikom dodavanja na watchlist: {e}")

    def open_watchlist(self):
        """
        Otvara watchlist u novom tabu.
        """
        try:
            print("Skrolovanje stranice do vrha.")
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)  # Kratko kašnjenje kako bi se osiguralo da je stranica skrolovana do vrha

            print("Otvaranje watchlist u novom tabu.")
            watchlist_button_selector = "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.sc-2e66506f-0.dfkLgL > div.sc-d8ea16bb-0.hZhyvu > div:nth-child(3) > div > div.sc-d1ede7e3-0.sc-5d9fc2ce-0.bwRagp.eeQQNU.right-section-link-buttons > div > button > a > span"
            watchlist_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, watchlist_button_selector))
            )
            watchlist_button.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"))
            )
            print("Watchlist uspešno otvorena.")
        except Exception as e:
            print(f"Došlo je do greške prilikom otvaranja watchlist: {e}")

    def verify_watchlist(self, num_to_verify):
        """
        Verifikuje da su izabrane kriptovalute na Watchlist.
        
        :return: True ako su sve izabrane kriptovalute na watchlist, inače False.
        """
        try:
            print(f"Verifikacija {num_to_verify} kriptovaluta na watchlist.")
            watchlist_rows = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"))
            )
            if len(watchlist_rows) >= num_to_verify:
                print("Sve izabrane kriptovalute su na watchlist.")
                return True
            else:
                print("Nisu sve izabrane kriptovalute na watchlist.")
                return False
        except Exception as e:
            print(f"Došlo je do greške prilikom verifikacije watchlist: {e}")
            return False

    def run_test(self):
        """
        Izvršava test koji otvara veb stranicu, dodaje na listu praćenja i verifikuje watchlist.
        """
        print("Pokretanje testa.")
        self.open_coinmarketcap()
        num_to_add = random.randint(5, 10)
        self.add_to_watchlist(num_to_add)
        self.open_watchlist()
        if self.verify_watchlist(num_to_add):
            print("Test uspešan: Sve izabrane kriptovalute su na watchlist.")
        else:
            print("Test neuspešan: Nisu sve izabrane kriptovalute na watchlist.")
        self.driver.quit()
        print("Test završen.")

if __name__ == "__main__":
    driver_path = "C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver.exe"
    chrome_path = "C:\\Users\\Administrator\\Downloads\\chrome-win64\\chrome-win64\\chrome.exe"
    test = CoinMarketCapTest(driver_path, chrome_path)
    test.run_test()
