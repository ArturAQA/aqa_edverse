from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_button = page.locator(MainLocators.AUTO_BUTTON)
        
    def click_login_button(self):
        """Кликнуть по кнопке Войти на главной странице"""
        self.login_button.click()
        return self