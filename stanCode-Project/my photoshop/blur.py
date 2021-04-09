"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    :param old_img: str, the file path of the original image
    :return: blurred image.
    """
    old = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(old.width, old.height)
    for y in range(old.height):
        for x in range(old.width):
            old_pixel = old.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x, y)
            if x == 0 and y == 0:
                new_pixel.red = (old.get_pixel(0, 1).red + old.get_pixel(1, 1).red +
                                 old.get_pixel(1, 0).red + old.get_pixel(x, y).red) // 4
                new_pixel.green = (old.get_pixel(0, 1).green + old.get_pixel(1, 1).green +
                                   old.get_pixel(1, 0).green + old.get_pixel(x, y).green) // 4
                new_pixel.blue = (old.get_pixel(0, 1).blue + old.get_pixel(1, 1).blue +
                                  old.get_pixel(1, 0).blue + old.get_pixel(x, y).blue) // 4
            elif x == 0 and y == (old.height - 1):
                new_pixel.red = (old.get_pixel(0, y - 2).red + old.get_pixel(1, y - 2).red +
                                 old.get_pixel(1, y - 1).red + old.get_pixel(x, y).red) // 4
                new_pixel.green = (old.get_pixel(0, y - 2).green + old.get_pixel(1, y - 2).green +
                                   old.get_pixel(1, y - 1).green + old.get_pixel(x, y).green) // 4
                new_pixel.blue = (old.get_pixel(0, y - 2).blue + old.get_pixel(1, y - 2).blue +
                                  old.get_pixel(1, y - 1).blue + old.get_pixel(x, y).blue) // 4
            elif x == (old.width - 1) and y == (old.height - 1):
                new_pixel.red = (old.get_pixel(x - 2, y - 2).red + old.get_pixel(x - 1, y - 2).red +
                                 old.get_pixel(x - 2, y - 1).red + old.get_pixel(x, y).red) // 4
                new_pixel.green = (old.get_pixel(x - 2, y - 2).green + old.get_pixel(x - 1, y - 2).green +
                                   old.get_pixel(x - 2, y - 1).green + old.get_pixel(x, y).green) // 4
                new_pixel.blue = (old.get_pixel(x - 2, y - 2).blue + old.get_pixel(x - 1, y - 2).blue +
                                  old.get_pixel(x - 2, y - 1).blue + old.get_pixel(x, y).blue) // 4
            elif x == (old.width - 1) and y == 0:
                new_pixel.red = (old.get_pixel(x - 2, 0).red + old.get_pixel(x - 1, 1).red +
                                 old.get_pixel(x - 2, 1).red + old.get_pixel(x, y).red) // 4
                new_pixel.green = (old.get_pixel(x - 2, 0).green + old.get_pixel(x - 1, 1).green +
                                   old.get_pixel(x - 2, 1).green + old.get_pixel(x, y).green) // 4
                new_pixel.blue = (old.get_pixel(x - 2, 0).blue + old.get_pixel(x - 1, 1).blue +
                                  old.get_pixel(x - 2, 1).blue + old.get_pixel(x, y).blue) // 4
            elif x == 0:
                new_pixel.red = (old.get_pixel(x + 1, y).red + old.get_pixel(x, y - 1).red +
                                 old.get_pixel(x, y + 1).red + old.get_pixel(x + 1, y - 1).red +
                                 old.get_pixel(x + 1, y + 1).red + old.get_pixel(x, y).red) // 6
                new_pixel.green = (old.get_pixel(x + 1, y).green + old.get_pixel(x, y - 1).green +
                                   old.get_pixel(x, y + 1).green + old.get_pixel(x + 1, y - 1).green +
                                   old.get_pixel(x + 1, y + 1).green + old.get_pixel(x, y).green) // 6
                new_pixel.blue = (old.get_pixel(x + 1, y).blue + old.get_pixel(x, y - 1).blue +
                                  old.get_pixel(x, y + 1).blue + old.get_pixel(x + 1, y - 1).blue +
                                  old.get_pixel(x + 1, y + 1).blue + old.get_pixel(x, y).blue) // 6

            elif x == (old.width - 1):
                new_pixel.red = (old.get_pixel(x - 1, y).red + old.get_pixel(x, y).red +
                                 old.get_pixel(x - 1, y - 1).red + old.get_pixel(x, y - 1).red +
                                 old.get_pixel(x - 1, y + 1).red + old.get_pixel(x, y + 1).red) // 6
                new_pixel.green = (old.get_pixel(x - 1, y).green + old.get_pixel(x, y).green +
                                   old.get_pixel(x - 1, y - 1).green + old.get_pixel(x, y - 1).green +
                                   old.get_pixel(x - 1, y + 1).green + old.get_pixel(x, y + 1).green) // 6
                new_pixel.blue = (old.get_pixel(x - 1, y).blue + old.get_pixel(x, y).blue +
                                  old.get_pixel(x - 1, y - 1).blue + old.get_pixel(x, y - 1).blue +
                                  old.get_pixel(x - 1, y + 1).blue + old.get_pixel(x, y + 1).blue) // 6

            elif y == 0:
                new_pixel.red = (old.get_pixel(x - 1, y).red + old.get_pixel(x + 1, y).red +
                                 old.get_pixel(x - 1, y + 1).red + old.get_pixel(x, y + 1).red +
                                 old.get_pixel(x + 1, y + 1).red + old.get_pixel(x, y).red) // 6
                new_pixel.green = (old.get_pixel(x - 1, y).green + old.get_pixel(x + 1, y).green +
                                   old.get_pixel(x - 1, y + 1).green + old.get_pixel(x, y + 1).green +
                                   old.get_pixel(x + 1, y + 1).green + old.get_pixel(x, y).green) // 6
                new_pixel.blue = (old.get_pixel(x - 1, y).blue + old.get_pixel(x + 1, y).blue +
                                  old.get_pixel(x - 1, y + 1).blue + old.get_pixel(x, y + 1).blue +
                                  old.get_pixel(x + 1, y + 1).blue + old.get_pixel(x, y).blue) // 6
            elif y == (old.height - 1):
                new_pixel.red = (old.get_pixel(x - 1, y).red + old.get_pixel(x + 1, y).red +
                                 old.get_pixel(x - 1, y - 1).red + old.get_pixel(x, y - 1).red +
                                 old.get_pixel(x + 1, y - 1).red + old.get_pixel(x, y).red) // 6
                new_pixel.green = (old.get_pixel(x - 1, y).green + old.get_pixel(x + 1, y).green +
                                   old.get_pixel(x - 1, y - 1).green + old.get_pixel(x, y - 1).green +
                                   old.get_pixel(x + 1, y - 1).green + old.get_pixel(x, y).green) // 6
                new_pixel.blue = (old.get_pixel(x - 1, y).blue + old.get_pixel(x + 1, y).blue +
                                  old.get_pixel(x - 1, y - 1).blue + old.get_pixel(x, y - 1).blue +
                                  old.get_pixel(x + 1, y - 1).blue + old.get_pixel(x, y).blue) // 6

            else:
                new_pixel.red = (old.get_pixel(x - 1, y).red + old.get_pixel(x + 1, y).red +
                                 old.get_pixel(x - 1, y - 1).red + old.get_pixel(x, y - 1).red +
                                 old.get_pixel(x - 1, y + 1).red + old.get_pixel(x, y + 1).red +
                                 old.get_pixel(x + 1, y - 1).red + old.get_pixel(x + 1, y + 1).red
                                 + old.get_pixel(x, y).red) // 9
                new_pixel.green = (old.get_pixel(x - 1, y).green + old.get_pixel(x + 1, y).green +
                                   old.get_pixel(x - 1, y - 1).green + old.get_pixel(x, y - 1).green +
                                   old.get_pixel(x - 1, y + 1).green + old.get_pixel(x, y + 1).green +
                                   old.get_pixel(x + 1, y - 1).green + old.get_pixel(x + 1, y + 1).green
                                   + old.get_pixel(x, y).green) // 9
                new_pixel.blue = (old.get_pixel(x - 1, y).blue + old.get_pixel(x + 1, y).blue +
                                  old.get_pixel(x - 1, y - 1).blue + old.get_pixel(x, y - 1).blue +
                                  old.get_pixel(x - 1, y + 1).blue + old.get_pixel(x, y + 1).blue +
                                  old.get_pixel(x + 1, y - 1).blue + old.get_pixel(x + 1, y + 1).blue +
                                  old.get_pixel(x, y).blue) // 9

    return new_img


def main():
    """
    This program blurs the image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
