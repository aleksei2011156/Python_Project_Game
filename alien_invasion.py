import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Класс для управления ресурсами и поведения игры. """

    def __init__(self):
        """ Инициализирует игру и создает игровые русурсы. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

            #Создание корабля
        self.ship = Ship(self)

        # Назначем цвет фона


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
                self._check_events()
                self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить корабль в право.
                    self.ship.rect.x += 1

    def _update_screen(self):
        """Обновляет изображение на экране и отоюбражает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Отслеживание последнего прорисованного экрана.
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()


