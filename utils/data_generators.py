from faker import Faker

# Создаем экземпляр библиотеки Faker на русском языке (чтобы данные были красивыми)
fake = Faker("ru_RU")


def generate_login_page_user():
    """Генерирует случайную почту и случайный пароль для негативных тестов."""
    return {"email": fake.email(), "password": fake.password(length=12)}
