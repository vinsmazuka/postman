import random
from string import ascii_letters
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from selenium import webdriver
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

new_account_dict = vars(new_account)
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
#
# driver.get('https://mail.ru/')
#
# register_btn = driver.find_element_by_xpath('//*[@id="mailbox"]/div[2]/a')
# register_btn.click()

