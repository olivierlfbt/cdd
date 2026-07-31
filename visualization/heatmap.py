import cv2
import numpy as np


class Heatmap:

    def generate(self, image, zones):

        mask = np.zeros(
            image.shape[:2],
            dtype=np.uint8
        )

        for zone in zones:

            cv2.rectangle(

                mask,

                (zone["x"], zone["y"]),

                (
                    zone["x"] + zone["width"],
                    zone["y"] + zone["height"]
                ),

                255,

                -1

            )

        heatmap = cv2.applyColorMap(
            mask,
            cv2.COLORMAP_JET
        )

        return cv2.addWeighted(
            image,
            0.7,
            heatmap,
            0.3,
            0
        )
