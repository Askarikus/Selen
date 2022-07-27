from unittest import TestCase

from service.functions.base_functions import main_menu_send_sharp


class ManFunctionsTestCase(TestCase):
    def test_main_menu_send_sharp(self):
        result = main_menu_send_sharp()
        self.assertEqual(' Привет.\n\nНа связи бот сервиса Wahelp,', result)
