from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('/home/klaybson/robos/chromedriver')

driver.get("https://klaybson.com.br/")