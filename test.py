from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


options = Options()

driver = Chrome(service=Service(r"C:\Users\BABAR\Desktop\chromedriver-win64\chromedriver.exe"), options=options)

# print(ChromeDriverManager().install())

driver.get('https://www.google.com/')