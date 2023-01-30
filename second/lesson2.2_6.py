import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element(By.ID, "input_value").text
print("1: ", a)
x = int(a)
print("2: ", x)
b = calc(x)
print("3: ", b)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element(By.ID, "answer").send_keys(b)
browser.find_element(By.ID, "robotCheckbox").click()
input1 = browser.find_element(By.ID, "robotsRule").click()

button = browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(10)
browser.quit()