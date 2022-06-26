from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


button_ = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button_book = browser.find_element(By.ID, "book")
button_book.click()


cur_x = browser.find_element(By.ID, "input_value")
x_ans = calc(int(cur_x.text))
ans_form = browser.find_element(By.ID, "answer")
ans_form.send_keys(x_ans)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(5)
browser.quit()

