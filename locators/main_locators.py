class MainLocators:
    """Локаторы для главной страницы Cinescope"""
    # Кнопки общего интерфейса
    AUTO_BUTTON = "[data-qa-id='login_page_button']"
    SHOW_MORE_BUTTON = ("button", "Показать еще")
    # Заголовок "Последние фильмы"
    LAST_MOVIES = ("heading", "Последние фильмы")
    # Карточка фильма
    MOVIE_CARD = ".bg-card.text-card-foreground"
    # Элементы внутри карточки фильма
    MOVIE_TITLE = "heading"
    MOVIE_POSTER = "img"
    MOVIE_DESCRIPTION = "paragraph"
    READ_MORE_BUTTON = "[data-qa-id='more_button']"
    # Переход на страницу со всеми фильмами
    ALL_MOVIES = ("link", "Все фильмы")
    # Перход на главную страницу сайта
    MAIN_PAGE = ("link", "Cinescope")