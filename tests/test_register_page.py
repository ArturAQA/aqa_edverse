import allure
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from utils.data_generators import generate_register_page_user

@allure.title("Тест регистрации с фейковыми данными")
@allure.feature("Регистрация")
def test_register_with_fake_data(page: Page):
    user = generate_register_page_user()
    register_page = RegisterPage(page).open("https://edversemovie.ru/register")
    
    with allure.step("Вводим имя"):
        register_page.name_input.fill(user["name"])
        allure.attach(user["name"], name="Имя", attachment_type=allure.attachment_type.TEXT)
        
    with allure.step("Вводим email"):
        register_page.email_input.fill(user["email"])
        allure.attach(user["email"], name="Email", attachment_type=allure.attachment_type.TEXT)   
        
    with allure.step("Вводим пароль"):
        register_page.password_input.fill(user["password"])
        allure.attach(user["password"], name="Пароль", attachment_type=allure.attachment_type.TEXT)
        
    with allure.step("Повторно вводим пароль"):
        register_page.password_repeat_input.fill(user["password"])  
        
    with allure.step("Кликаем на кнопку Зарегистрироваться"):
        register_page.register_button.click()
        page.wait_for_timeout(1000)
        
    with allure.step("Проверяем результат"):
        expect(page).to_have_url("https://edversemovie.ru/register")              