from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
# Selenium проверяет в течение 12 секунд совпадение цены
    Optimalprice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100"))
# Нажать на кнопку Book
    book = browser.find_element(By.CSS_SELECTOR, "#book")
    book.click()

# Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
# Вставить найденное значение в окно ввода
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
# Нажать на кнопку Submit
    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

    print(browser.switch_to.alert.text)

finally:

    # закрываем браузер после всех манипуляций
    browser.quit()