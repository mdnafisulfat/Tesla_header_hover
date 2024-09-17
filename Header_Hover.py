import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.tesla.com/')

actions = ActionChains(driver)

header_element1 = driver.find_element(By.ID, 'dx-nav-item--vehicles')
actions.move_to_element(header_element1).perform()
time.sleep(2)

header_element2 = driver.find_element(By.ID, 'dx-nav-item--energy')
actions.move_to_element(header_element2).perform()
time.sleep(2)

header_element3 = driver.find_element(By.ID, 'dx-nav-item--charging')
actions.move_to_element(header_element3).perform()
time.sleep(2)

header_element4 = driver.find_element(By.ID, 'dx-nav-item--discover')
actions.move_to_element(header_element4).perform()
time.sleep(2)

header_element5 = driver.find_element(By.ID, 'dx-nav-item--shop')
actions.move_to_element(header_element5).perform()
time.sleep(2)

driver.quit()
