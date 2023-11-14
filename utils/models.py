import pygame


class GameElement:
    def __init__(self, name: str, image_path: str, screen_dim: tuple, step: float=1.0) -> None:
        self.name = name
        self.image = pygame.image.load(image_path)
        size = self.image.get_size()
        self.width = size[0]
        self.height = size[1]
        self.screen_width = screen_dim[0]
        self.screen_height = screen_dim[1]
        self.x = 0
        self.y = 0
        self.step = step
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_visible = True

    def set_step(self, step: float) -> None:
        self.step = step

    def keep_moving_left(self) -> None:
        if self.is_moving_left and self.can_move_left():
            self.move_left()

    def keep_moving_right(self) -> None:
        if self.is_moving_right and self.can_move_right():
            self.move_right()

    def can_move_left(self) -> bool:
        return self.x >= self.step

    def can_move_right(self) -> bool:
        return self.x <= self.screen_width - self.width - self.step

    def can_move_up(self) -> bool:
        return self.y >= self.step

    def can_move_down(self) -> bool:
        return self.y <= self.screen_height - self.height - self.step

    def move_left(self) -> None:
        self.is_moving_left = True
        self.move_by_x(self.x - self.step)

    def move_right(self) -> None:
        self.is_moving_right = True
        self.move_by_x(self.x + self.step)

    def stop_moving_left(self) -> None:
        self.is_moving_left = False

    def stop_moving_right(self) -> None:
        self.is_moving_right = False

    def set_position(self, x: int, y: int) -> None:
        self.move_by_x(x)
        self.move_by_y(y)

    def move_by_x(self, x: int) -> None:
        self.x = x

    def move_by_y(self, y: int) -> None:
        self.y = y

    def show(self) -> None:
        self.is_visible = True

    def hide(self) -> None:
        self.is_visible = False    
