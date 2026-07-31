import cv2
import numpy as np


class VegetationIndex:

    def calculate(self, image):

        blue, green, red = cv2.split(image)

        green = green.astype(np.float32)
        red = red.astype(np.float32)

        index = (green - red) / (
            green + red + 1e-5
        )

        return index
