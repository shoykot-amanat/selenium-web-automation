import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoPopupHandler():
    def demo_popuphandler(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='myFunction()']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Selenium")
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

dpopup = DemoPopupHandler()
dpopup.demo_popuphandler()