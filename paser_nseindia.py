import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.nseindia.com/')
sleep(5)

# Ищем MARKET DATA ID
menu_items = driver.find_element(By.CSS_SELECTOR, "#link_2")

counterSleep = 0
while not menu_items.is_displayed():
    sleep(1)
    counterSleep += 1
    if counterSleep > 25:
        print("Page unreachable")
        exit(4)

# Раскрываем MARKET DATA
actions = ActionChains(driver)
actions.move_to_element(menu_items).perform()

# Ожидаем открытия меню и ищем item Pre-Open Market
pre_open = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(driver.find_element(By.LINK_TEXT, 'Pre-Open Market'))
)

# Кликаем на item Pre-Open Market
actions.click(pre_open).perform()
sleep(5)

# Скачиваем csv
button_element = driver.find_element(By.XPATH, "//a[@onclick='downloadPreopen()']")
button_element.click()

# Ждем загрузку файла
counterSleep = 0
while not button_element.is_displayed():
    sleep(1)
    counterSleep += 1
    if counterSleep > 5:
        print("link unreachable")
        exit(5)

# Определение пути к папке "Загрузки"
download_path = os.path.expanduser("~") + "/Downloads"

# Пользовательский сценарий
home = driver.find_element(By.ID, "link_0")
home.click()

# Ожидаем загрузку страницы
sleep(2)
element = driver.find_element(By.CLASS_NAME,"fa-brands")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

driver.quit()



