from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option=Options()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(chrome_options=option,service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com")