import cv2

from config import (
    HEALTHY_COLOR,
    DISEASE_COLOR
)


class Overlay:

    def draw(self, image, zones):

        frame = image.copy()

        for zone in zones:

            color = DISEASE_COLOR

            if zone["risk"] == "Low":
                color = HEALTHY_COLOR

            cv2.rectangle(

                frame,

                (zone["x"], zone["y"]),

                (
                    zone["x"] + zone["width"],
                    zone["y"] + zone["height"]
                ),

                color,

                2

            )

            cv2.putText(

                frame,

                zone["risk"],

                (
                    zone["x"],
                    zone["y"] - 10
                ),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                color,

                2

            )

        return frame
