import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_ebyTest():


    driver= webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    SearchBox= driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    SearchBox.send_keys("16 GB HP Laptop")



    SearchButton= driver.find_element(By.ID,"gh-btn")
    SearchButton.click();

    #WebDriverWait(driver,timeout=15).until(EC.text_to_be_present_in_element(By.XPATH,"//h1[@class='srp-controls__count-heading')],"16 GB HP Laptop")
