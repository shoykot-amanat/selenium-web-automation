import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys module

class DemoScreenShot():
    def demo_screenshot(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(4)
        driver.get_screenshot_as_file("facebook.png")
        log_in = driver.find_element(By.XPATH, "//button[@id='u_0_5_uT']")
        log_in.click()
        time.sleep(4)
        driver.get_screenshot_as_file("facebook_login.png")
        driver.save_screenshot("facebook_login2.png")
        driver.quit()

dss = DemoScreenShot()
dss.demo_screenshot()