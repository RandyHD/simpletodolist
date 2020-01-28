from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках
        self.assertIn('To-Do', self.browser.title)

        self.fail('Закончить тест!')
        # Ей сразу же предлагается ввести элемент списка

        # Она набирает в текстовом поле "Купить павлиньи перья"
        # Когда она нажимает enter, страница обновляется, и теперь страница содержит
        # "1: Купить павлиньи перья" в качестве элемента списка
        # Текстовое поле по-прежнему приглашает её добавить ещё один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # Страница снова обновляется, и теперь показывает оба элемента её списка
        # Эдит интересно, запомнит ли сайт её список. Далее она видит, что
        # сайт сгенерировал для неё уникальный URL-адрес - об этом
        # выводится небольшой текст с объяснениями.
        # Она посещает этот URL-адрес - её список по-прежнему там

        # Удовлетворенная, она снова ложится спать

if __name__ == '__main__':
    unittest.main()
