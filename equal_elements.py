import os 

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


