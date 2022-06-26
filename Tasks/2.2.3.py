from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements(By.TAG_NAME, "input")
labels = browser.find_elements(By.XPATH, "//input[contains(@class, 'from-control')]")

count = 0
for i, el in enumerate(elements):
    el.send_keys("123")
    count += 1
    if count == 3:
        break

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

check_file = browser.find_element(By.ID, "file")
check_file.send_keys(file_path)

button = browser.find_element(By.XPATH, "//button[@type]")
button.click()

time.sleep(5)
browser.quit()