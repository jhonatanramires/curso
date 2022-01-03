from ursina import * 
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

player = PlatformerController2d(y = 1, z  x = .01 )
ground=Entity(model='quad', y=- 2, scale_x=10, collider="box", color=color.yellow )

app.run()

