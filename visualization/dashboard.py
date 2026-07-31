import cv2

from config import WINDOW_TITLE
from visualization.overlay import Overlay


class Dashboard:

    def __init__(self):

        self.overlay = Overlay()

    def show(self, image, zones):

        frame = self.overlay.draw(
            image,
            zones
        )

        cv2.imshow(
            WINDOW_TITLE,
            frame
        )

        cv2.waitKey(1)

    def close(self):

        cv2.destroyAllWindows()
