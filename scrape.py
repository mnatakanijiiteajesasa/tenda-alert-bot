from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import time
from selenium.webdriver.common.by import By

    
def scrape_tenders(url):

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(url)
        time.sleep(10)
        tenders_button = driver.find_element(By.LINK_TEXT, "Tenders")
        tenders_button.click()
        time.sleep(5)
        all_tenders_button = driver.find_element(By.LINK_TEXT, "ALL TENDERS")
        all_tenders_button.click()
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        
    finally:
        driver.quit()

def clean_content(content):
    soup = BeautifulSoup(content, "html.parser")

    for remove_ss in soup(["scrypt"], ["style"]):
        remove_ss.extract()

    valid_content = soup.get_text(separator = "\n")
    valid_content = "\n".join(line.strip() for line in valid_content.splitlines() if line.strip())
    

    return valid_content

tenders = []

