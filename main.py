from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

FB_EMAIL = 'YOUR FACEBOOK LOGIN EMAIL'
FB_PASSWORD = 'YOUR FACEBOOK PASSWORD'

chrome_driver_path = 'YOUR CHROME DRIVER PATH'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

sleep(2)
fb_login = driver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
