import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = " https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

number1 = browser.find_element(By.ID, 'num1')
number_1 = int(number1.text)
print("1:", number_1)
number2 = browser.find_element(By.ID, 'num2')
number_2 = int(number2.text)
print("2:", number_2)

y = number_1 + number_2
print("HAhahahahah: ", y)

browser.find_element(By.ID, "dropdown").send_keys(y)

input1 = browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(10)
browser.quit()