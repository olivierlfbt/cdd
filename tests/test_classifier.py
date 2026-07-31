import unittest
import numpy as np

from core.health_classifier import HealthClassifier


class HealthClassifierTest(unittest.TestCase):

    def test_classification(self):

        contour = np.array([
            [[0, 0]],
            [[0, 100]],
            [[100, 100]],
            [[100, 0]]
        ])

        classifier = HealthClassifier()

        result = classifier.classify([contour])

        self.assertEqual(
            len(result),
            1
        )

        self.assertIn(
            "risk",
            result[0]
        )


if __name__ == "__main__":
    unittest.main()
