import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# **********Function to select multiple items in an multi select box **********************
# **** This is basic function *******
# ****For enhanced function   refer to file -> " MultiSelectInputBox_E1.py "  ****


def select_values(elements_list, values_to_select):
    for e in elements_list:
        e_text_value = e.get_attribute('text')
        for v in values_to_select:
            if e_text_value == v:
                driver.find_element(By.XPATH, "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//li[text()='"+v+"']").click()
                time.sleep(2)
                break
#*********************End of function************************

#****************Below code are to test above function is working fine **************************
driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/admin/")
driver.maximize_window()

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),' Customers')]").click()
driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/Create']").click()

ele = driver.find_element(By.ID,"AdminComment")
driver.execute_script("arguments[0].scrollIntoView()",ele)

driver.find_element(By.XPATH,"//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div/input").click()
elements = driver.find_elements(By.XPATH,"//select[@id='SelectedCustomerRoleIds']/option")

print(len(elements))

for e in elements:
    print(e.get_attribute('text'))

# ************Calling function with multiple values to be selected**************************
select_values(elements, ['Administrators','Forum Moderators','Salesman'])

driver.save_screenshot("..\\Screenshots\\MultiSelectInputBox.png")
driver.close()