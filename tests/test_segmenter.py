import unittest
import numpy as np

from core.disease_segmenter import DiseaseSegmenter


class DiseaseSegmenterTest(unittest.TestCase):

    def setUp(self):

        self.segmenter = DiseaseSegmenter()

    def test_segment_returns_list(self):

        image = np.zeros(
            (400, 400),
            dtype=np.uint8
        )

        result = self.segmenter.segment(image)

        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
