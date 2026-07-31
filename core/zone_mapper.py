import cv2


class ZoneMapper:

    def build(self, image, classified_regions):

        zones = []

        for region in classified_regions:

            x, y, w, h = cv2.boundingRect(
                region["contour"]
            )

            zones.append({

                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "risk": region["risk"],
                "area": region["area"]

            })

        return zones
