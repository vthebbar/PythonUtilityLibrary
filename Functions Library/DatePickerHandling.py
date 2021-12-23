# This is to handle date picker calendar,  conditions such as february, leap year,
# ...future date selection and past date selection is also handled
#  Application : https://jqueryui.com/datepicker/
# This is Initial work,  Enhanced code work is in ->  DatePickerCalendarHandling.py

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def get_month_year(month_year):
    return month_year.split(" ")

def get_month_value(month_name):
    month_value = 0
    month_dict = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,
                  "September":9,"October":10,"November":11,"December":12}

    for key,value in month_dict.items():
        if key == month_name:
            month_value = int(value)

    return month_value


def select_date(expected_day, expected_month, expected_year):

    driver.get("https://jqueryui.com/datepicker/")
    driver.maximize_window()
    driver.switch_to.frame(0)
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"datepicker").click()

    #time.sleep(2)

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID, "ui-datepicker-div")))

    month_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-title")
    print(month_year)
    print(month_year.text)
    month_year = month_year.text.strip()
    month_year_list = month_year.split(" ")
    print(month_year_list)
    month = month_year_list[0]
    year = month_year_list[1]
    print(month)
    print(year)

    month_value = get_month_value(expected_month)
    if month_value in [1,3,5,7,8,10, 12]:
        if int(expected_day) > 31:
            print("Invalid date:", expected_day,expected_month, expected_year)
            return
    if month_value in [4,6,9,11]:
        if int(expected_day) > 30:
            print("Invalid date:", expected_day,expected_month, expected_year)
            return

    if expected_month == "February":
        if int(expected_year) % 4 == 0:
            if int(expected_day) > 29:
                print("Invalid date :",expected_day, expected_month, expected_year)
                return
        else:
            if int(expected_day) > 28:
                print("Invalid date :",expected_day, expected_month, expected_year)
                return

    while (month != expected_month or year != expected_year):

        if int(year) < int(expected_year):
            driver.find_element(By.XPATH,"//a[@title='Next']").click()
            #time.sleep(2)
            month_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-title")
            month_year = month_year.text.strip()
            month_year_list = month_year.split(" ")
            month = str(month_year_list[0])
            year = str(month_year_list[1])

        elif int(year) > int(expected_year):
            driver.find_element(By.XPATH, "//a[@title='Prev']").click()
            # time.sleep(2)
            month_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-title")
            month_year = month_year.text.strip()
            month_year_list = month_year.split(" ")
            month = str(month_year_list[0])
            year = str(month_year_list[1])

        elif int(year) == int(expected_year):
            expected_month_value = get_month_value(expected_month)
            current_month_value = get_month_value(month)
            if expected_month_value > current_month_value:
                driver.find_element(By.XPATH, "//a[@title='Next']").click()
                # time.sleep(2)
                month_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-title")
                month_year = month_year.text.strip()
                month_year_list = month_year.split(" ")
                month = str(month_year_list[0])
                year = str(month_year_list[1])

            elif expected_month_value < current_month_value:
                driver.find_element(By.XPATH, "//a[@title='Prev']").click()
                # time.sleep(2)
                month_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-title")
                month_year = month_year.text.strip()
                month_year_list = month_year.split(" ")
                month = str(month_year_list[0])
                year = str(month_year_list[1])

            elif expected_month_value == current_month_value:
                pass


    try:
        driver.find_element(By.XPATH,"//a[text()='"+str(expected_day)+"']").click()

    except Exception as e:
        print("Invalid date:", e)


#v = get_month_year("January 2024")
#print(v)
#print(v[1])

select_date("28","February","2025")