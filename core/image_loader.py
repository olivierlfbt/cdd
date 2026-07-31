import cv2

from config import IMAGE_PATH


class ImageLoader:

    def load(self):

        image = cv2.imread(str(IMAGE_PATH))

        if image is None:
            raise FileNotFoundError(
                f"Unable to load image: {IMAGE_PATH}"
            )

        return image
