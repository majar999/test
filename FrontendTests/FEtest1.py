from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoinMarketCapTest:
    """
    Class to test the CoinMarketCap webpage functionality using Selenium WebDriver.
    """

    def __init__(self, driver_path, chrome_path):
        """
        Initializes the WebDriver.
        
        :param driver_path: Path to the WebDriver executable.
        :param chrome_path: Path to the Chrome executable.
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
        print("WebDriver initialized successfully.")

    def open_coinmarketcap(self):
        """
        Opens the CoinMarketCap website.
        """
        try:
            print("Opening CoinMarketCap website.")
            self.driver.get("https://coinmarketcap.com")
            print("Website opened successfully.")
        except Exception as e:
            print(f"An error occurred while opening the website: {e}")

    def click_all(self):
        """
        Clicks the 'All' button to display all results.
        """
        try:
            print("Attempting to click 'All' button.")
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            all_button = next(button for button in buttons if button.text.strip() == 'All')
            self.driver.execute_script("arguments[0].click();", all_button)
            print("'All' button clicked successfully using JavaScript.")
        except Exception as e:
            print(f"An error occurred while clicking 'All': {e}")
            self.driver.quit()

    def verify_all_results_displayed(self):
        """
        Verifies that all results are displayed after clicking 'All'.
        
        :return: True if all results are displayed, otherwise False.
        """
        try:
            print("Verifying that all results are displayed.")
            results = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "cmc-table-row"))
            )
            print(f"Number of results found: {len(results)}")
            return len(results) > 0
        except Exception as e:
            print(f"An error occurred while verifying results: {e}")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            return False

    def run_test(self):
        """
        Runs the test to open the webpage, click 'All', and verify the results.
        """
        print("Starting test.")
        self.open_coinmarketcap()
        self.click_all()
        if self.verify_all_results_displayed():
            print("Test passed: All results are displayed.")
        else:
            print("Test failed: Results are not displayed.")
        self.driver.quit()
        print("Test completed.")

if __name__ == "__main__":
    driver_path = "C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver.exe"
    chrome_path = "C:\\Users\\Administrator\\Downloads\\chrome-win64\\chrome-win64\\chrome.exe"
    test = CoinMarketCapTest(driver_path, chrome_path)
    test.run_test()
