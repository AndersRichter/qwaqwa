import os

import unittest

from tests.pages.auth import AuthPage
from tests.pages.main import MainPage
from tests.pages.message import MessagePage
from tests.pages.dialog import DialogPage
from tests.pages.dialog_menu import DialogMenuPage
from tests.pages.confirm import ConfirmPage
from time import sleep
from selenium.webdriver import DesiredCapabilities, Remote


class TestsStickers(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.BOT_1_LOGIN = "technopark3"
        self.PASSWORD = os.environ['PASSWORD']
        self.CURRENT_DIALOG_URL = ""
        self.STICKERS_NEW_SET_ID = "2"
        self.STICKERS_OLD_SET_ID = "35"
        self.STICKERS_PAY_SET_ID = "42"

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()

        self.create_dialog()
        self.CURRENT_DIALOG_URL = self.driver.current_url

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.delete_dialog()
        self.driver.quit()

    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()

    def delete_dialog(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

    def test_send_usmile_sticker(self):
        self.dialog_page.send_sticker("USMILE_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_usmile_sticker failed")

    def test_send_usmile_2_sticker(self):
        self.dialog_page.send_sticker("USMILE_STICKER_2")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_usmile_2_sticker failed")

    def test_send_dog_sticker(self):
        self.dialog_page.send_sticker("DOG_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_dog_sticker failed")

    def test_send_fox_sticker(self):
        self.dialog_page.send_sticker("FOX_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_fox_sticker failed")

    def test_send_heart_sticker(self):
        self.dialog_page.send_sticker("HEART_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_heart_sticker failed")

    # You have my respect, Stark. When I'm done, half of
    # humanity will still be alive. I hope they remember you.

    def test_add_stickers_set(self):
        set_id = self.STICKERS_NEW_SET_ID
        self.assertFalse(
            self.dialog_page.check_stickers_set(set_id),
            "testing stickers set already exists")
        self.dialog_page.install_stickers_set(set_id)
        self.assertTrue(
            self.dialog_page.check_stickers_set(set_id),
            "can't add new sticker set #" + set_id)
        self.dialog_page.uninstall_stickers_set(set_id)

    def test_delete_sticker_set(self):
        set_id = self.STICKERS_OLD_SET_ID
        self.assertTrue(
            self.dialog_page.check_stickers_set(set_id),
            "default stickers set is not exist")
        self.dialog_page.uninstall_stickers_set(set_id)
        self.assertFalse(
            self.dialog_page.check_stickers_set(set_id),
            "Can't delete sticker set #" + set_id)
        self.dialog_page.install_stickers_set(set_id)

    def test_add_paid_stickers_set(self):
        set_id = self.STICKERS_PAY_SET_ID
        self.assertFalse(
            self.dialog_page.check_stickers_set(set_id),
            "pay stickers set already exists #" + set_id)
        self.dialog_page.install_stickers_set(set_id)
        self.assertTrue(
            self.dialog_page.check_stickers_set(set_id),
            "can't add new pay sticker set #" + set_id)
        self.dialog_page.uninstall_stickers_set(set_id)
