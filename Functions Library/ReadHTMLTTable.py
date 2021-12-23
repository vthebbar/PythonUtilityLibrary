# Read Data from HTML table

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://vthebbar.blogspot.com/2021/12/hml-table.html")
driver.maximize_window()

table_xpath = "//div[@id='post-body-8812568829104001243']/table/tbody"

# **************  function ******************
def print_table(table_xpath):
    rows_xpath = table_xpath +"/tr"
    cols_xpath = table_xpath + "/tr[2]/td"
    rows = driver.find_elements(By.XPATH,rows_xpath)
    cols = driver.find_elements(By.XPATH, cols_xpath)
    num_of_rows = len(rows)
    num_of_cols = len(cols)
    print("Number of rows=", num_of_rows)
    print("Number of colums=", num_of_cols)

    # Print headers outside the loop
    print("Contact                  Company                    Country")
    for r in range(2,num_of_rows+1):
        for c in range(1, num_of_cols+1):
            tab_element = driver.find_element(By.XPATH,
                        "//div[@id='post-body-8812568829104001243']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            print(tab_element, end="                        ")
        print()

# calling the function
print_table(table_xpath)
driver.close()


#******* Rough work ************************
'''
e=table.find_element(By.XPATH,"//div[@id='post-body-8812568829104001243']/table/tbody/tr[1]/th[1]")
print(e.text)

rows = driver.find_elements(By.XPATH,"//div[@id='post-body-8812568829104001243']/table/tbody/tr")
number_of_rows = len(rows)
print("Number of rows=", number_of_rows)

cols = driver.find_elements(By.XPATH,"//div[@id='post-body-8812568829104001243']/table/tbody/tr[1]/th")
number_of_cols = len(cols)
print("Number of columns=", number_of_cols)

print("Contact                  Company                    Country")
print("***********Table Values*****************")
for r in range(2,number_of_rows+1):
    for c in range(1,number_of_cols+1):
        table_element = driver.find_element(By.XPATH,
                            "//div[@id='post-body-8812568829104001243']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(table_element, end="                         ")
    print()

driver.close()
'''
