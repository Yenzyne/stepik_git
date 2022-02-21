from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



link = "http://suninjuly.github.io/explicit_wait2.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return math.log(abs(12*math.sin(int(x))))


    # first_num = browser.find_element(By.CSS_SELECTOR, "input_value")
    # result_one = first_num.text
    # second_num = browser.find_element(By.CSS_SELECTOR, "#num2")
    # result_two = second_num.text
    #
    #
    # res = calc(result_one, result_two)
    #
    # print(result_one, result_two, res)
    #
    # # input1 = browser.find_element(By.CSS_SELECTOR, "#dropdown")
    # # input1.click()
    #
    # select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    # select.select_by_value(res)  # ищем элемент с текстом "Python"
    # input1 = browser.find_element(By.CSS_SELECTOR, ".trollface")
    # input1.click()
    #
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)



    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    input1 = browser.find_element(By.CSS_SELECTOR, "#book")
    input1.click()

    # confirm = browser.switch_to.alert
    # confirm.accept()


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    result = x_element.text
    x = result
    y = calc(x)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)


    # input1 = browser.find_element(By.NAME, ".btn-primary")
    # input1.click()
    #
    # confirm = browser.switch_to.alert
    # confirm.accept()
    #
    # input2 = browser.find_element(By.NAME, "lastname")
    # input2.send_keys("Mak")
    # input3 = browser.find_element(By.NAME, "email")
    # input3.send_keys("deumon128@gmail.com")
    #
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')
    #
    # input4 = browser.find_element(By.CSS_SELECTOR, "[accept='.txt']")
    # input4.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "form button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

