import pygame

DEFAULT_FONT = 'font.ttf'


class Scene:
    """
    Базовый класс, от которого наследуются сцены
    """

    def __init__(self, controller):
        """
        :param controller: Ссылка на объект контроллера, к которому относится сцена
        """
        self.controller = controller
        self.sprites = {}
        self.labels = {}
        self.buttons = {}

    def on_update(self) -> None:
        """
        Функция вызывается при обновлении сцены
        """

    def on_event(self, event: pygame.event) -> None:
        """
        Функция вызывается при получении сценой события
        """

    def on_draw(self, screen) -> None:
        """
        Функция вызывается при отрисовке сцены, отрисовывает все надписи, спрайты и кнопки
        """
        for sprite in self.sprites.keys():
            self.controller.screen.blit(self.sprites[sprite]['image'], self.sprites[sprite]['rect'])
        for button in self.buttons.keys():
            self.controller.screen.blit(self.buttons[button]['image'], self.buttons[button]['image_rect'])
            self.controller.screen.blit(self.buttons[button]['text'], self.buttons[button]['text_rect'])
        for label in self.labels.keys():
            self.controller.screen.blit(self.labels[label]['label'], self.labels[label]['rect'])

    def add_sprite_to_scene(self, name: str, image: str, center: tuple[int, int], size: tuple[int, int], transparency: bool = False) -> None:
        """
        Метод добавления спрайтов на сцену (в словарь self.sprites)
        :param name: Название спрайта (ключ в словаре)
        :param image: Путь к картинке спрайта
        :param center: Позиционирование спрайта (от центра (x, y))
        :param transparency: Имеет ли спрайт альфа-слой прозрачности
        """
        self.sprites[name] = {}
        if transparency:
            self.sprites[name]['image'] = pygame.image.load(image).convert_alpha()
        else:
            self.sprites[name]['image'] = pygame.image.load(image).convert()
        self.sprites[name]['image'] = pygame.transform.scale(self.sprites[name]['image'], size)
        self.sprites[name]['rect'] = self.sprites[name]['image'].get_rect()
        self.sprites[name]['rect'].center = center

    def add_label_to_scene(self, name: str, font_color: tuple[int, int, int], font_size: int,
                           font: str = DEFAULT_FONT, center: tuple[int, int] = (0, 0),
                           text: str = '') -> None:
        """
        Метод для добавления надписей на сцену (в словарь self.labels)
        :param name: Название надписи (ключ в словаре)
        :param font_color: Цвет шрифта надписи
        :param font_size: Размер шрифта
        :param font: Шрифт надписи
        :param center: Позиционирование надписи (от центра (x, y))
        :param text:  Текст надписи
        """
        font_object = pygame.font.Font(font, font_size)
        label = font_object.render(text, True, font_color)
        rect = label.get_rect()
        rect.center = center
        self.labels[name] = {}
        self.labels[name]['label'] = label
        self.labels[name]['rect'] = rect

    def add_button_to_scene(self, name: str, font_color: tuple[int, int, int], font_size: int, text: str,
                            font: str = DEFAULT_FONT, center: tuple[int, int] = (0, 0),
                            width: int = 0) -> None:
        """
        Метод для добавления кнопок на сцену (в словарь self.buttons)
        :param name: Название кнопки (ключ в словаре), нужно для обработчика событий
        :param font_color: Цвет надписи на кнопке
        :param font_size: Размер шрифта надписи на кнопке
        :param text: Текст надписи на кнопке
        :param font: Шрифт надписи на кнопке
        :param center: Позиционирование кнопки (от центра (x, y))
        :param width: Необязательный параметр. Если установлен - ширина кнопки будет соответствовать ему. Иначе подстроится под ширину надписи
        """
        image = pygame.image.load('button.png').convert_alpha()
        font_object = pygame.font.Font(font, font_size)
        text_surface = font_object.render(text, True, font_color)
        text_size = text_surface.get_size()
        if width == 0:
            image = pygame.transform.scale(image, (text_size[0] + 30, text_size[1] + 20))
        else:
            image = pygame.transform.scale(image, (width, text_size[1] + 20))
        text_rect = text_surface.get_rect()
        text_rect.center = center
        rect = image.get_rect()
        rect.center = center
        self.buttons[name] = {}
        self.buttons[name]['image'] = image
        self.buttons[name]['image_rect'] = rect
        self.buttons[name]['text'] = text_surface
        self.buttons[name]['text_rect'] = text_rect
