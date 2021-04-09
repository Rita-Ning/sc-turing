"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image.
    :return: mirror lake picture.
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, img.height * 2)

    for y in range(img.height):
        for x in range(img.width):
            # data
            img_pixel = img.get_pixel(x, y)

            # Empty pixel1
            new_pixel1 = blank_img.get_pixel(x, y)
            # create pixel 2
            new_pixel2 = blank_img.get_pixel(x, blank_img.height - 1 - y)

            new_pixel1.red = img_pixel.red
            new_pixel1.green = img_pixel.green
            new_pixel1.blue = img_pixel.blue

            new_pixel2.red = img_pixel.red
            new_pixel2.green = img_pixel.green
            new_pixel2.blue = img_pixel.blue

    return blank_img


def main():
    """
    This program makes the picture flip vertically
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()







if __name__ == '__main__':
    main()
