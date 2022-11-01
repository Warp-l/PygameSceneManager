import pygame
from pygame import MOUSEBUTTONUP

from scene import Scene


class MainScene(Scene):
    """
      Сцена № 1
      """

    def __init__(self, controller) -> None:
        Scene.__init__(self, controller)

    def create_buttons(self) -> None:
        """
        Метод, добавляющий кнопки на сцене
        """
        self.add_button_to_scene(name='next_screen_button', font_color=(25, 25, 25), font_size=42,
                                 text='На следующий экран', center=(400, 300))
        self.add_button_to_scene(name='quit_button', font_color=(25, 25, 25), font_size=42,
                                 text='Выход', center=(400, 500))

    def create_sprites(self) -> None:
        """
        Метод, добавляющий на сцену спрайты
        """
        self.add_sprite_to_scene(name='big_bg', image='main_bg.jpg', center=(400, 300), size=(800, 600), transparency=False)
        self.add_sprite_to_scene(name='bg', image='main_big_bg.jpg', center=(400, 400), size=(450, 350), transparency=False)


    def create_labels(self) -> None:
        """
        Метод, добавляющий на сцену надписи
        """
        label = "Welcome to the SceneManager"
        self.add_label_to_scene(name='title', font_color=(255, 255, 255), font_size=32, center=(400, 40),
                                text=label)


    def on_update(self) -> None:
        """
        Метод-обработчик обновления сцены
        """
        pass

    def on_event(self, event: pygame.event) -> None:
        """
        Метод-обработчик событий
        :param event:
        """
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if self.buttons['next_screen_button']['image_rect'].collidepoint(event.pos):
                self.controller.change_scene(self.controller.scenes['second_scene'])
            if self.buttons['quit_button']['image_rect'].collidepoint(event.pos):
                self.controller.quit()

    def on_draw(self, screen) -> None:
        """
        Метод, отвечающий за отрисовку сцены
        """
        self.create_buttons()
        self.create_sprites()
        self.create_labels()
        super(MainScene, self).on_draw(screen)