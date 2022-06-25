import pygame


def load_image(texture_path: str, width: int, height: int):
    image = pygame.image.load(f"../res/{texture_path}")
    image = pygame.transform.scale(image, (width, height))

    return image
