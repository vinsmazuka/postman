import csv
import os
import random
import zipfile
from string import ascii_letters
from anticaptchaofficial.imagecaptcha import imagecaptcha
from anticaptcha_secret_key import API_KEY
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender


class Account:
    """представляет аккаунт электронной почты"""
    pass

    def __init__(
            self,
            name,
            surname,
            birth_day,
            birth_month,
            birth_year,
            account_name,
            password
    ):
        self.name = name
        self.surname = surname
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.account_name = account_name
        self.password = password


class AntiCaptcha:
    """используется для считывания текста капчи"""
    solver = imagecaptcha()
    solver.set_key(API_KEY)

    def __init__(self, path):
        """инициализирует экземпляр класса
        :param path: путь к файлу с изображением капчи(тип- str)
        """
        self.file_path = path

    def return_text(self):
        """возвращает текст капчи, либо текст ошибки"""
        captcha_text = self.solver.solve_and_return_solution(self.file_path)
        if captcha_text != 0:
            return captcha_text
        else:
            return f"task finished with error {self.solver.error_code}"


class RandomAccount:
    """Представляет случайный аккаунт"""
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

    @classmethod
    def generate(cls):
        """генерирует случайный аккаунт и возвращает словарь с данными о нем"""
        rand_name = cls.new_person.name(gender=Gender.MALE)
        rand_surname = cls.new_person.surname(gender=Gender.MALE)
        rand_day = str(random.randint(1, 28))
        rand_month = random.choice(cls.months)
        rand_year = str(random.randint(1970, 2003))
        rand_account_name = ''.join(random.choice(cls.account_name_symbols) for i in range(12))
        rand_password = ''.join(random.choice(cls.password_symbols) for i in range(12))
        result = {
            'rand_name': rand_name,
            'rand_surname': rand_surname,
            'rand_day': rand_day,
            'rand_month': rand_month,
            'rand_year': rand_year,
            'rand_account_name': rand_account_name,
            'rand_password': rand_password
        }
        return result


class CsvWriter:
    """
    Предназначен для записи данных в CSV файл
    """
    pass

    @staticmethod
    def write(path, new_account):
        """
        Записывает данные о созданном аккаунте в указанный файл CSV
        :param path: путь к файлу, в кот необходимо произвести запись
        :param new_account: словарь, содержащий информацию о об аккаунте
        :return возвращает сообщение об ошибке, если возникла ошибка
        """
        headers = list(new_account.keys())
        try:
            with open(path, "a", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=headers)
                writer.writerow(new_account)
        except PermissionError:
            message = (f'запись в файл не была осуществлена, т.к. файл {path} был открыт,'
                       ' закроте файл и повторите попытку')
            return message
        else:
            message = f'была осуществлена запись в файл {path}'
            return message


class Archivator:
    """используется для создания архивов"""
    archivator = zipfile.ZipFile

    @classmethod
    def make_archive(cls, items, path='', archive='project.zip'):
        """
        перезаписывает архив
        :param items: список элементов, которые необходимо заархивировать(тип - list)
        :param path: путь, по которому необходимо сохранить архив(тип - str)
        :param archive: имя архива(тип - str)
        :return: имя архива(тип - str)
        """
        def inner():
            """создает архив"""
            with cls.archivator(archive, mode='w') as zf:
                for item in items:
                    add_item = os.path.join(path, item)
                    zf.write(add_item)
        if archive in os.listdir():
            os.remove(archive)
            items = os.listdir()
            inner()
            return archive
        else:
            inner()
            return archive


if __name__ == '__main__':
    file = Archivator.make_archive(items=os.listdir())
    print(file)
