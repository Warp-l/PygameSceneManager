import pygame
import scene_manager

manager = scene_manager.SceneManager()


def main():
    manager.loop()


if __name__ == '__main__':
    pygame.init()
    manager.change_scene(manager.scenes['main_scene'])
    main()
