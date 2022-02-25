import random
import time
from string import ascii_letters
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from selenium import webdriver
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
rand_account_name = ''.join(random.choice(account_name_symbols) for i in range(8))
rand_password = ''.join(random.choice(password_symbols) for i in range(8))

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
name_field = driver.find_element(by=By.XPATH, value='//*[@id="fname"]')
surname_field = driver.find_element(by=By.XPATH, value='//*[@id="lname"]')
name_field.send_keys(rand_name)
surname_field.send_keys(rand_surname)
time.sleep(60)
driver.quit()


