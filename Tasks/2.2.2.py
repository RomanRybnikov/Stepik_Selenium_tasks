from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

cur_x = browser.find_element(By.ID, "input_value")

x_ans = calc(int(cur_x.text))

browser.execute_script("window.scrollBy(0, 100);")

button = browser.find_element(By.XPATH, "//button[@type]")

ans_form = browser.find_element(By.ID, "answer")

ans_form.send_keys(x_ans)

cb = browser.find_element(By.ID, "robotCheckbox")
cb.click()

rb = browser.find_element(By.ID, "robotsRule")
rb.click()

button.click()

time.sleep(10)
browser.quit()