# Multi Select dropdown checkboxes
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#*****************Generic Function to select multiple checkboxes******************
def select_items(elements_list, items_to_select):
    for e  in elements_list:
        element_text = e.text
        print(element_text)
        for i in items_to_select:
            if element_text == i:
                driver.find_element(By.XPATH,"//div[@id='skills_checklist']/ul/li/input[@value='"+str(i)+"']").click()
                break

# ********************** Testing of above function *********************

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demo.yourblogcoach.com/s/jquery-multiselect-dropdown/?q=download&_ga=2.201424018.203949997.1640255813-1593477150.1640255813")
#wait = WebDriverWait(driver,10)
name_ele= driver.find_element(By.ID,"name")
driver.execute_script("arguments[0].scrollIntoView()", name_ele)
time.sleep(2)
#wait.until(ec.visibility_of_element_located((By.ID,"button")))
elements = driver.find_elements(By.XPATH,"//div[@id='skills_checklist']/ul/li")
select_items(elements, ['C++','Java','XML'])

time.sleep(5)
driver.close()