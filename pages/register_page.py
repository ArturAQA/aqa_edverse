from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.register_locators import RegisterLocators

class RegisterPage(BasePage):
    """Страница регистрации."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.name_input = page.locator(RegisterLocators.NAME_INPUT)
        self.email_input = page.locator(RegisterLocators.EMAIL_INPUT)
        self.password_input = page.locator(RegisterLocators.PASSWORD_INPUT)
        self.password_repeat_input = page.locator(RegisterLocators.PASSWORD_REPEAT_INPUT)
        self.register_button = page.locator(RegisterLocators.REGISTER_BUTTON)
        
    def register(self, name: str, email: str, password: str):
        """Заполняет форму регистрации и нажимает «Зарегистрироваться»."""
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.password_repeat_input.fill(password)
        self.register_button.click()
        return self
    