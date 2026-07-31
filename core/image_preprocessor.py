import cv2

from config import GAUSSIAN_KERNEL


class ImagePreprocessor:

    def process(self, image):

        blurred = cv2.GaussianBlur(
            image,
            GAUSSIAN_KERNEL,
            0
        )

        return blurred
