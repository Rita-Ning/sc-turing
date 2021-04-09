"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""


from simpleimage import SimpleImage


def combine(space_ship, figure):
    """
    :param background_img: space ship image
    :param figure_img: figure image.
    :return: figure with background image.
    """
    for y in range(figure.height):
        for x in range(figure.width):
            pixel_figure = figure.get_pixel(x, y)
            bigger = max(pixel_figure.red, pixel_figure.blue)
            if pixel_figure.green > (bigger * 2):
                pixel_bg = space_ship.get_pixel(x, y)
                pixel_figure.red = pixel_bg.red
                pixel_figure.blue = pixel_bg.blue
                pixel_figure.green = pixel_bg.green
    return figure


def main():
    """
    This program makes the green screen into other background scene.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()



if __name__ == '__main__':
    main()
