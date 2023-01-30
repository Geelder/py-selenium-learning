import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

alert = browser.switch_to.alert
alert.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text
print("haha: ", x)
b = calc(x)
print("hehe: ", b)

browser.find_element(By.ID, "answer").send_keys(b)

button = browser.find_element(By.CLASS_NAME, "btn").click()


time.sleep(10)
browser.quit()