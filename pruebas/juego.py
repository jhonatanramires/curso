from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
                model = 'cube',
                color = color.white,
                texture = 'white_cube',
                rotation = Vec3(45,45,45)
                )

class Test_button(Entity):
    def __init__(self):
        super().__init__(
                model = 'cube',
                texture = 'brick_texture',
                color = color.blue
                )


def update():
    if held_keys['a']:
        test_square.x -= 1 * time.dt

app = Ursina()

app.run()
