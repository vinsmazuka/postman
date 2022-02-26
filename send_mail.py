import random
import time
from string import ascii_letters
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import core

new_person = Person(locale=Locale.RU)
account_name_symbols = ascii_letters + '0123456789'
password_symbols = account_name_symbols + '()_'
months = [
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь'
    ]

rand_name = new_person.name(gender=Gender.MALE)
rand_surname = new_person.surname(gender=Gender.MALE)
rand_day = str(random.randint(1, 28))
rand_month = random.choice(months)
rand_year = str(random.randint(1970, 2003))
rand_account_name = ''.join(random.choice(account_name_symbols) for i in range(12))
rand_password = ''.join(random.choice(password_symbols) for i in range(12))

new_account = core.Account(
    name=rand_name,
    surname=rand_surname,
    birth_day=rand_day,
    birth_month=rand_month,
    birth_year=rand_year,
    account_name=rand_account_name,
    password=rand_password
)

new_account_info = vars(new_account)

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://mail.ru/')

register_btn = driver.find_element(by=By.XPATH, value='/html/body/main/div[2]/div[1]/div[1]/div[2]/div[2]/a')
register_btn.click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.set_window_size(600, 700)

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


time.sleep(30)
driver.quit()


