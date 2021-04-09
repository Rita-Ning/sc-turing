"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image.
    :return img: SimpleImage, the shrink image.
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width // 2, img.height // 2)

    for y in range(img.height):
        for x in range(img.width):
            # data
            if (x + y) % 2 == 1:
                img_pixel = img.get_pixel(x, y)

                # empty new pixel
                new_pixel = blank_img.get_pixel(x//2, y//2)

                new_pixel.red = img_pixel.red
                new_pixel.green = img_pixel.green
                new_pixel.blue = img_pixel.blue

    return blank_img


def main():
    """
    This program shrinks its height and width to 1/2.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
