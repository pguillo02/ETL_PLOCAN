import os
import shutil

def equal_elements(route):
    """
    Function designed to compare the number of images and labels in a given directory. If both categories are equal it prints the total number
    of images and labels on the screen. If they are not it generates the corresponding empty label for isolated images and deletes the label 
    in case of isolated (useless) tags. It also prints on the screen a summary of the actions performed and the new number of images and labels.

    This function is prepared to work with a given structure of route --> images/labels --> selected data. For adapting different folder structures
    use the proper functions in the load module. 

    Args:

        route: str = Directory in which the images and labels are contain.

    """

    images_path: str = os.path.join(route, "images")
    labels_path: str = os.path.join(route, "labels")

    for image in os.listdir(images_path):
        pass


def jpg_to_jpeg(route):
    """
    Function designed to transform a jpg image into a jpeg image. 

    Args 
        route: str = Directory where the images to be changed are located.
    """
    
    for item in os.listdir(route):
        image: str = os.path.join(route, item)
        new_image: str = os.path.join(route, item.replace(".jpg", ".jpeg"))
        os.rename(image, new_image)

        print(f'Image {image} renamed to {new_image}')


def empty_tags(route: str, tagging_folder: str):
    """
    Function designed for sending untagged images to a specific folder.

    Args: 
        route: str = Directory where the images to be checked are located.
        tagging_folder: str = Directory where untaged images are copied.
    """

    labels: str = os.path.join(route, "labels")
    images: str = os.path.join(route, "images")

    os.makedirs(tagging_folder, exist_ok=True)

    for tag in os.listdir(labels):
        label_path: str = os.path.join(labels, tag)
        image_path: str = os.path.join(images, tag.replace(".txt", ".jpeg"))

        if os.path.getsize(label_path) == 0:
            shutil.copyfile(image_path, os.path.join(tagging_folder, tag.replace(".txt", ".jpeg")))
            print(f'Image {image_path} copied to the tagging folder')     
