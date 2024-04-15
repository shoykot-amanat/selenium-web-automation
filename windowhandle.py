import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys module

class DemoWindowHandler():
    def demo_windowhandler(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        parent_window = driver.current_window_handle
        print("Parent window handle: ", parent_window)
        driver.find_element(By.XPATH, "//a[@title='Flat 13% OFF (up to Rs. 2,200)']//span[contains(text(),'Domestic Flights')]").click()
        time.sleep(4)
        all_windows = driver.window_handles
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print("Child window handle: ", window)
                time.sleep(4)
                driver.close()
                time.sleep(3)
                break

dwh = DemoWindowHandler()
dwh.demo_windowhandler()

