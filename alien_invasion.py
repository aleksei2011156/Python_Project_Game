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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

            #Создание корабля
        self.ship = Ship(self)

        # Назначем цвет фона


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
                self._check_events()
                self._update_screen()
                self.ship.update()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    #Рефакторинг _check_events_
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиши."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпуск клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False





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


