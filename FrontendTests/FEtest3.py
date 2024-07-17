from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Inicijalizacija WebDriver-a
driver = webdriver.Chrome()

try:
    # 1. Otvori stranicu
    driver.get("https://coinmarketcap.com/")
    
    # Postavi prozor pretraživača na full screen
    driver.maximize_window()
    
    # Čekaj da se stranica učita
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # 2. Prikazivanje padajućeg menija na kartici "Cryptocurrencies"
    cryptocurrencies_tab = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.sc-2e66506f-0.dfkLgL > div.sc-d8ea16bb-0.hZhyvu > div:nth-child(3) > div > div.sc-19cbbba9-2.jJjjqr > div.sc-19cbbba9-3.bdecVu > section > div:nth-child(1) > a > div"))
    )
    
    # Simuliraj prelazak miša preko "Cryptocurrencies" taba
    actions = ActionChains(driver)
    actions.move_to_element(cryptocurrencies_tab).perform()
    
    # Dodatno čekanje da se meni učita
    time.sleep(2)
    
    # 3. Klik na "Ranking" opciju iz dropdown menija
    option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Ranking']"))
    )
    option.click()
    
    # 4. Zapisivanje podataka sa trenutne stranice
    table_selector = "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"
    table = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, table_selector))
    )
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        print(row.text)
    
    # Čekaj 2 sekunda 
    time.sleep(2)
    
    # 5. Klik na dugme "Filters"
    filter_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-d577b7d4-4.dZhWhQ > div.sc-4c05d6ef-0.sc-c652d51c-1.sc-6fa8c3d4-0.dlQYLv.jOvctx.eDTcwB.table-control-outer-wrapper.scroll-indicator.scroll-initial.hideArrow > div.scroll-child > div.sc-4c05d6ef-0.dlQYLv.table-control-area > div > button.sc-7d96a92a-0.bvcvhD.sc-c652d51c-0.eDtVLJ.table-control-filter"))
    )
    filter_button.click()
    print("Dugme Filter je kliknuto.")
    
    # 6. Klik na dugme "Category"
    category_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > ul > li:nth-child(1) > div > span > button"))
    )
    category_button.click()
    print("Dugme Category je kliknuto.")
    
    # 7. Korišćenje trake za pretragu unutar padajućeg menija da se ukuca "Platform" i pritisne Enter
    search_bar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']"))
    )
    search_bar.send_keys("Platform")
    search_bar.send_keys(Keys.ENTER)
    print("Opcija Platform je odabrana.")
    
    # 8. Provera podataka sa primenjenim filterom
    filtered_data = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.sc-2e66506f-1.buMEwe.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-963bde9f-2.bZVSBs > table"))
    )
    filtered_rows = filtered_data.find_elements(By.TAG_NAME, "tr")
    for row in filtered_rows:
        print(row.text)

finally:
    # Zatvaranje WebDriver-a
    driver.quit()
