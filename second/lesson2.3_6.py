import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CLASS_NAME, "trollface").click()

new_window = browser.window_handles[1]
print("1 window: ", new_window)

browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text
print("haha: ", x)
b = calc(x)
print("hehe: ", b)
time.sleep(1)

browser.find_element(By.ID, "answer").send_keys(b)

time.sleep(1)


button = browser.find_element(By.CLASS_NAME, "btn").click()


time.sleep(10)
browser.quit()