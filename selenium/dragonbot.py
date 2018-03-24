from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://kderoulet.github.io/dragonfighter/')

input_element = driver.find_element_by_tag_name('input')
input_element.send_keys('1' + Keys.RETURN)
