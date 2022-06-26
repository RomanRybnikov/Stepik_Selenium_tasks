from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element_radio = browser.find_element(By.ID, "treasure")
x_ = x_element_radio.get_attribute("valuex")
x_ans = calc(x_)

inp = browser.find_element(By.ID, "answer")
inp.send_keys(x_ans)

checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
checkbox_robot.click()

radio_btn = browser.find_element(By.ID, "robotsRule")
radio_btn.click()

submit = browser.find_element(By.XPATH, "//button[@type]")
submit.click()

time.sleep(10)

browser.quit()