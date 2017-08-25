#
# ps7pr4.py (Problem Set 7, Problem 4)
#
# Image processing with loops and image objects
#
# Computer Science 111
# 

from cs111png import *

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###

def grayscale(filename):
    """ Takes a png upload and converts each pixel to grayscale by setting each
pixel to the brightness. Then converting the final product to a new filename
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # grayscale the colors of the pixel at row r, column c
            new_rgb = [brightness(rgb), brightness(rgb),brightness(rgb)]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'grayscale_' + filename
    img.save(new_filename)


#Part 2

def fold_diag(filename):
    """ Takes a png upload and set the half image to white.
    Then converting the final product to a new filename
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):

            # Set the pixel to white if the row is greater than the column
            new_rgb = [255, 255, 255]
            if r > c:
                img.set_pixel(r,c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'fold_diag_' + filename
    img.save(new_filename)


def flip_vert(filename):
    """ Takes an image and flip the image by converting the pixel to the opposite
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height, width)
    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_img.set_pixel(height - 1-r, width -1 -c , rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'flipv_' + filename
    new_img.save(new_filename)
