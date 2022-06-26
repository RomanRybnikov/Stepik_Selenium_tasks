from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

x_ans = calc(x)
inp = browser.find_element(By.ID, "answer")

inp.send_keys(x_ans)

checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
checkbox_robot.click()
radio_btn = browser.find_element(By.ID, "robotsRule")
radio_btn.click()

submit = browser.find_element(By.XPATH, "//button[@type]")
submit.click()
# y = calc(x)
# print(y)

time.sleep(10)

browser.quit()