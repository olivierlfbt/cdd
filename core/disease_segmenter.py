import cv2
import numpy as np

from config import (
    SEGMENTATION_THRESHOLD,
    MIN_REGION_AREA
)


class DiseaseSegmenter:

    def segment(self, vegetation_index):

        normalized = cv2.normalize(
            vegetation_index,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        ).astype(np.uint8)

        _, mask = cv2.threshold(
            normalized,
            SEGMENTATION_THRESHOLD,
            255,
            cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        regions = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area >= MIN_REGION_AREA:

                regions.append(contour)

        return regions
