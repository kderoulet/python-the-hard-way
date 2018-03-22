from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org')

second_browser = webdriver.Chrome()
second_browser.get('http://seleniumhq.org')