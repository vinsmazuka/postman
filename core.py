from anticaptchaofficial.imagecaptcha import imagecaptcha
from anticaptcha_secret_key import API_KEY


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

if __name__ == '__main__':
    text = AntiCaptcha(path='captcha.jpg').return_text()
    print(text)