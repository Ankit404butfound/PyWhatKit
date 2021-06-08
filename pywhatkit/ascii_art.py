from PIL import Image


def image_to_ascii_art(imgpath: str, output_file: str = "pywhatkit_asciiart.txt") -> str:
    """Converts the given image to ascii art and save it to output_file"""
    # pass the image as command line argument
    image_path = imgpath
    img = Image.open(image_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    # write to a text file.
    with open(output_file, "w") as f:
        f.write(ascii_image)
    return ascii_image
