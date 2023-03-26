"""
Writer: Ranel Ben Simman Tov
"""
import numpy as np
from PIL import Image

IMAGE_PATH = "code.png"


def decrypt(img_path):
    """
    decrypt the image by finding the black pixels indices
    :param img_path: the path to the image
    :return: the decrypted message
    """
    img = Image.open(img_path)
    img_arr = np.array(img)
    black_pixels = np.argmax(img_arr == 1, axis=0)
    char_list = [chr(i) for i in black_pixels]
    return ''.join(char_list)


if __name__ == "__main__":
    # test the decrypt function
    # Place gunpowder beneath the House of Lords. 11/05/1605
    print(decrypt(IMAGE_PATH))



