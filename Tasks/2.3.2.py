from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.XPATH, "//button[@type]")
button.click()

alert = browser.switch_to.alert
alert.accept()

cur_x = browser.find_element(By.ID, "input_value")
x_ans = calc(int(cur_x.text))
ans_form = browser.find_element(By.ID, "answer")
ans_form.send_keys(x_ans)

button = browser.find_element(By.XPATH, "//button[@type]")
button.click()

time.sleep(5)
browser.quit()