from streamlit import camera_input, image, expander
from PIL import Image


with expander('Start Camera'):
    # Start the camera
    camera_image = camera_input('Camera')

    if camera_image:
        # Created a Pillow image instance
        image_instance = Image.open(camera_image)

        # L is one of the algorithms that converts an image to gray scale
        grayImage = image_instance.convert('L')

        # Renders the image on the web page
        image(grayImage)
