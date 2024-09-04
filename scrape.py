from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import time
from selenium.webdriver.common.by import By

    
def scrape_tenders(url):

# setting up chrome driver options
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
#scraping tenders data from the tenders page
    try:
        driver.get(url)
        time.sleep(10)
    # finding and clicking the tenders button
        tenders_button = driver.find_element(By.LINK_TEXT, "Tenders")
        tenders_button.click()
        time.sleep(5)
    # finding the tenders table
        table = driver.find_element(By.TAG_NAME, "table")
        tenders = []
        count = 0
        
# looping through the tenders table rows
        for row in table.find_elements(By.XPATH, ".//tbody/tr"):
            if count >= limit:
                break
        # finding the tables's cells
            cells = row.find_elements(By.TAG_NAME, "td")
            
        # stripping the the required cells
            if len(cells) > 0:
                tender_no = cells[0].text.strip()
                description = cells[1].text.strip()
                procuring_entity = cells[2].text.strip()
                closing_date = cells[5].text.strip()

        # adding the stripped tenders data to our empty tender list
                tenders.append({
                    'Tender Number': tender_no,
                    'Description': description,
                    'Procuring Entity': procuring_entity,
                    'Closing Entity': closing_date
                    })
                count +=1

        return tenders
#stopping the automation    
    finally:
        driver.quit()

