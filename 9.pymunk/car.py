import arcade
import math
import pymunk
from game_object import Box

WIDTH = 800
HEIGHT = 800
TITLE = "boxes"

class Car:
    def __init__(self, x, y, space):
        # body
        mass = 5
        moment = pymunk.moment_for_box(mass, (100, 70))
        chassis_body = pymunk.Body(mass, moment)
        chassis_body.position = (x, y)
        # shape
        chassis_shape = pymunk.Poly.create_box(chassis_body, (100, 70))
        chassis_shape.elasticity = 0.3
        chassis_shape.friction = 0.5

        space.add(chassis_body, chassis_shape)

        self.chassis_sprite = arcade.SpriteSolidColor(100, 70, arcade.color.RED)

        self.sprites = arcade.SpriteList()
        self.sprites.append(self.chassis_sprite)
        self.chassis_body = chassis_body
        self.chassis_shape = chassis_shape
    
    def update(self):
        self.chassis_sprite.center_x = self.chassis_shape.body.position.x
        self.chassis_sprite.center_x = self.chassis_shape.body.position.y
        self.chassis_sprite.radians = self.chassis_shape.body.angle


class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        # crear espacio
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        self.car = Car(700, 400, self.space)

        # sprites
        self.sprites = arcade.SpriteList() 
        self.sprites.extend(self.car.sprites)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60) # OJO
        self.car.update()
        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()