from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.google.com')
assert 'Google' in browser.title

elem = browser.find_element_by_name('q')
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()