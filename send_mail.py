from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://mail.ru/')

register_btn = driver.find_element_by_xpath('//*[@id="mailbox"]/div[2]/a')
register_btn.click()

