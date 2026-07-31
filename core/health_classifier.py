import cv2


class HealthClassifier:

    def classify(self, contours):

        result = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > 4000:
                level = "High"

            elif area > 1500:
                level = "Medium"

            else:
                level = "Low"

            result.append({
                "contour": contour,
                "risk": level,
                "area": round(area, 2)
            })

        return result
