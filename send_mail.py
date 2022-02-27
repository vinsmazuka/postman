import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import core

rand_account = core.RandomAccount.generate()

new_account = core.Account(
    name=rand_account['rand_name'],
    surname=rand_account['rand_surname'],
    birth_day=rand_account['rand_day'],
    birth_month=rand_account['rand_month'],
    birth_year=rand_account['rand_year'],
    account_name=rand_account['rand_account_name'],
    password=rand_account['rand_password']
)

new_account_info = vars(new_account)
print(new_account_info)

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://mail.ru/')
time.sleep(2)
register_btn = driver.find_element(by=By.XPATH, value='/html/body/main/div[2]/div[1]/div[1]/div[2]/div[2]/a')
register_btn.click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.set_window_size(600, 700)
time.sleep(2)
name_field = driver.find_element(by=By.XPATH, value='//*[@id="fname"]')
surname_field = driver.find_element(by=By.XPATH, value='//*[@id="lname"]')
birth_day_selector = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/div[2]/div/div[1]/div/div/select")
birth_month_selector = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/div[2]/div/div[3]/div/select")
birth_year_selector = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/div[2]/div/div[5]/div/div/select")
gender_selector = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[8]/div[2]/div/label[1]/div[1]")
account_name_field = driver.find_element(by=By.XPATH, value='//*[@id="aaa__input"]')
password_field = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
create_btn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/button')

name_field.send_keys(rand_name)
surname_field.send_keys(rand_surname)
Select(birth_day_selector).select_by_visible_text(rand_day)
Select(birth_month_selector).select_by_visible_text(rand_month)
Select(birth_year_selector).select_by_visible_text(rand_year)
gender_selector.click()
account_name_field.send_keys(rand_account_name)
password_field.send_keys(rand_password)
time.sleep(2)
repeat_password_field = driver.find_element(by=By.XPATH, value='//*[@id="repeatPassword"]')
repeat_password_field.send_keys(rand_password)
create_btn.click()
time.sleep(10)

img = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/div[5]/img')
img_link = img.get_attribute('src')
driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[-1])
driver.get(str(img_link)+'.png')

with open('captcha.png', 'wb') as file:
    file.write(driver.find_element(by=By.TAG_NAME, value='img').screenshot_as_png)
driver.close()
driver.switch_to.window(driver.window_handles[1])

solver = core.AntiCaptcha('captcha.png')
captcha_text = solver.return_text()

captcha_inp_field = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/div[5]/div/div[1]/div/div/div/div/input')
captcha_inp_field.send_keys(captcha_text)

continue_btn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/button[1]')
continue_btn.click()

time.sleep(20)

cancel_btn = driver.find_element(by=By.XPATH, value='/html/body/div[16]/div[2]/div/div/div[2]/form/button[2]')
cancel_btn.click()

print(new_account_info)

time.sleep(300)
driver.quit()



