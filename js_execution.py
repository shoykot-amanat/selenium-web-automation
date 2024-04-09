import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys module

class DemoJsExecution():
    def demo_jsexecution(self):
        driver = webdriver.Chrome()
        driver.execute_script("window.open('https://training.rcvacademy.com/');")
        time.sleep(20)
        demo_element = driver.execute_script("return document.getElementsByClassName('dynamic-link')[2];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(5)

dje = DemoJsExecution()
dje.demo_jsexecution()