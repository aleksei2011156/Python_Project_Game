"""" Класс для хранения всех настройек игры."""
class Settings():
    def __init__(self):
        """Инициализирует статические найтроки игры."""
        # Параметр экрана.
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color  = (230, 230, 230)
        # Настройка корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 80
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройка пришельцев
        # self.alien_speed = 0.7
        self.fleet_drop_speed = 7


        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходу игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение в право; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale




