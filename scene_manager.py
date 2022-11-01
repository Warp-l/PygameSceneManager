import pygame
import main_scene
import second_scene

RESOLUTION = (800, 600)
CAPTION = 'PyGame Scene Manager Test'
FPS = 30


class SceneManager:
    """
        Контроллер игровых экранов, позволяющий переключаться между ними
        В блоке __init__ в self.scenes прописывается список сцен с именами
    """

    def __init__(self):
        self.scenes = {
        }
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(CAPTION)
        self.scene = None
        self.running = True
        self.clock = pygame.time.Clock()
        self.add_scenes()

    def add_scenes(self):
        """
        Добавление сцен в список сцен
        """
        self.scenes['main_scene'] = main_scene.MainScene(self)
        self.scenes['second_scene'] = second_scene.SecondScene(self)

    def loop(self) -> None:
        """
        Основной цикл контроллера, вызывает из сцен методы отрисовки, апдейта и реакции на события
        """
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                self.scene.on_event(event)
                if event.type == pygame.QUIT:
                    self.quit()

            self.scene.on_update()
            self.scene.on_draw(self.screen)

            pygame.display.flip()

    def change_scene(self, scene: str) -> None:
        """
        Метод, переключающий активную сцену
        :param scene: Название сцены (ключ) из словаря self.scenes
        """
        self.scene = scene

    def quit(self) -> None:
        """
        Завершение работы контроллера и, соответственно всей программы
        """
        self.running = False