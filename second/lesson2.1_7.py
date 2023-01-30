import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math



link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


treasure = browser.find_element(By.ID, "treasure")
atr = treasure.get_attribute('valuex')

x =  atr
print("On est!: ", x)
y = calc(x)
print("HAHA: ", y)

inputvalue = browser.find_element(By.ID, "answer")
inputvalue.send_keys(y)


input1 = browser.find_element(By.ID, "robotCheckbox")
input1.click()

input2 = browser.find_element(By.ID, "robotsRule")
input2.click()

input3 = browser.find_element(By.CLASS_NAME, 'btn')
input3.click()

time.sleep(10)
browser.quit()