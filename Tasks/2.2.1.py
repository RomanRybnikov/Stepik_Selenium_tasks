from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element(By.ID, "num1")
x2 = browser.find_element(By.ID, "num2")
cur_sum = int(x1.text) + int(x2.text)
cur_sum = str(cur_sum)
print(cur_sum)

select = Select(browser.find_element(By.ID, "dropdown"))

fin_sum_ = select.select_by_value(cur_sum)

submit = browser.find_element(By.XPATH, "//button[@type]")
submit.click()


time.sleep(10)
browser.quit()
