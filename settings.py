"""" Класс для хранения всех настройек игры."""
class Settings():
    def __init__(self):
        """Инициализирует найтроки игры."""
        # Параметр экрана.
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color  = (230, 230, 230)
        # Настройка корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)


