import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDropdownMultipleSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        dropdown = driver.find_element(By.ID, "multi-select")
        dd_multi = Select(dropdown)

        dd_multi.select_by_index(1)
        time.sleep(2)
        dd_multi.select_by_value("New Jersey")
        time.sleep(3)
        dd_multi.select_by_visible_text("Texas")
        time.sleep(3)
        dd_multi.deselect_by_index(1)
        time.sleep(2)
        driver.quit()

ddd = DemoDropdownMultipleSelect()
ddd.demo_dropdown()