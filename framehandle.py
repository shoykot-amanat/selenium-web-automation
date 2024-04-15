import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoFrameHandler():
    def demo_framehandler(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
        driver.maximize_window()
        time.sleep(4)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='W3Schools Free Online Web Tutorials']"))
        driver.find_element(By.XPATH, "//a[@title='CSS Tutorial'][normalize-space()='CSS']").click()
        time.sleep(4)

dframe = DemoFrameHandler()
dframe.demo_framehandler()