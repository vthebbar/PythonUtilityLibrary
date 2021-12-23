# Handle multi select box, Click CONTROL and Select

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://vthebbar.blogspot.com/2021/12/multi-select-dropdown-with-checkbox.html")
driver.implicitly_wait(5)

all_items = driver.find_elements(By.XPATH,"//select[@id='languages']/option")

def select_items(list_of_items, items_to_select):
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).perform()
    for l in list_of_items:
        item = l.text
        print("item=",item)
        for i in items_to_select:
            print("i=",i)
            if item == i:
                driver.find_element(By.XPATH, "//select[@id='languages']/option[text()='"+str(i)+"']").click()
                action.key_up(Keys.CONTROL).perform()

select_items(all_items, ['PHP','Python','.Net'])

time.sleep(4)
driver.close()