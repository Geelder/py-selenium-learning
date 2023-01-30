import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

        
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
print("1:", file_path)


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.NAME, "firstname").send_keys("Ivan")
last_name = browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
email = browser.find_element(By.NAME, "email").send_keys("Ivan@mail.ru")


browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)



button = browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(10)
browser.quit()