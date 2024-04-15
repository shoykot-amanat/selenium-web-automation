import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoDropdownSingleSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.NAME, "UserTitle")

        dd = Select(dropdown)
        dd.select_by_index(2)
        time.sleep(2)
        dd.select_by_value("CxO_General_Manager_ANZ")
        time.sleep(3)
        dd.select_by_visible_text("Customer Service Manager")
        time.sleep(3)
        driver.quit()
ddd = DemoDropdownSingleSelect()
ddd.demo_dropdown()

