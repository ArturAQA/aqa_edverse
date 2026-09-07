import pytest  # Импортируем pytest для создания фикстур
import allure  # Импортируем Allure для скриншотов
from playwright.sync_api import sync_playwright  # Импортируем менеджер контекста Playwright


@pytest.fixture(scope="session")  # Одна фикстура на весь прогон
def browser():
    """Один браузер на весь прогон — не нужно открывать его для каждого теста."""
    with sync_playwright() as p:  # Открываем контекст Playwright
        b = p.chromium.launch(headless=False)  # Графический режим (видим браузер)
        yield b
        b.close()  # Закрываем браузер


@pytest.fixture()  # Новая фикстура для каждого теста (по умолчанию)
def context(browser):
    """Изолированный контекст на каждый тест: чистые cookies и localStorage."""
    ctx = browser.new_context()
    yield ctx
    ctx.close()


@pytest.fixture()
def page(context):
    """Новая страница (вкладка) для каждого теста."""
    pg = context.new_page()
    yield pg
    pg.close()


# Хук для автоматического создания скриншотов в Allure при падении теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )