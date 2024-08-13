import arcade
from bresenham import get_line, get_circle

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Primitivas de arcade"


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 10
        
    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()

    
if __name__ == "__main__":
    app = MyWindow()
    arcade.run()