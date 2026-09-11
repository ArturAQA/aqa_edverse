class RegisterLocators:
    """Локаторы для страницы регистрации Cinescope"""
    
    # Заголовок "Регистрация"
    REGISTER_HEADING = ("heading", "Регистрация")
    
    # Поля ввода
    NAME_INPUT = "[data-qa-id='register_full_name_input']"
    EMAIL_INPUT = "[data-qa-id='register_email_input']"
    PASSWORD_INPUT = "[data-qa-id='register_password_input']"
    PASSWORD_REPEAT_INPUT = "[data-qa-id='register_password_repeat_input']"
    
    # Кнопки
    REGISTER_BUTTON = "[data-qa-id='register_submit_button']"
    
    # Переход на главную страницу сайта
    MAIN_PAGE = ("link", "Cinescope")
        
    # Переход на страницу со всеми фильмами
    ALL_MOVIES = ("link", "Все фильмы")
    
    # Переход на страницу авторизации
    LOGIN_LINK = ("link", "Войти")
