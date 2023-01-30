import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math



link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "[ID='input_value']")
x =  x_element.text
y = calc(x)

inputvalue = browser.find_element(By.ID, "answer")
inputvalue.send_keys(y)


input1 = browser.find_element(By.ID, "robotCheckbox")
input1.click()

input2 = browser.find_element(By.CSS_SELECTOR, '[ID="robotsRule"]')
input2.click()

input3 = browser.find_element(By.CLASS_NAME, 'btn')
input3.click()

time.sleep(10)
browser.quit()