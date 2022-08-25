from PIL import Image
import os

# This script creates a .webp copy of all .png, .jpg, and .jpeg images in this
# repository for faster web loading.


# Images to be converted.
convertable = ['jpg', 'jpeg', 'png']


def convert_image_to_webp(
        path,
) -> None:
    """
    Convert an image file (.png, .jpg, .jpeg) to a webp file.
    :param path: Path to image.
    :return: None
    """

    base, ext = os.path.splitext(path)
    if ext[1:] in convertable:
        image = Image.open(path)
        new_path = base + '.wepb'
        image.save(new_path, format='webp')
        print(f'created {new_path}')


def convert_all_images_to_webp():
    """
    Convert all images in directories to webp.
    :return: None
    """

    # Define paths to loop through
    repo = os.path.dirname(os.getcwd())
    directories = [
        os.path.join(repo, 'images'),
        os.path.join(repo, 'images', 'articles'),
        os.path.join(repo, 'images', 'research'),
    ]

    # Loop through all paths, images
    for directory in directories:
        for file in os.listdir(directory):
            if file.split('.')[-1] in convertable:
                convert_image_to_webp(
                    path=os.path.join(directory, file)
                )



if __name__ == '__main__':
    convert_all_images_to_webp()