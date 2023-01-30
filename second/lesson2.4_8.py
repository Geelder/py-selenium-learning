import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
print("1.: ", price)
browser.find_element(By.ID, "book").click()

browser.execute_script("window.scrollBy(0, 400);")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text
print("haha: ", x)
b = calc(x)
print("hehe: ", b)

browser.find_element(By.ID, "answer").send_keys(b)

time.sleep(1)


submit_button =  browser.find_element(By.ID, "solve")
submit_button.click()

time.sleep(10)
browser.quit()