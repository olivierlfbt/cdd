import unittest
import numpy as np

from core.zone_mapper import ZoneMapper


class ZoneMapperTest(unittest.TestCase):

    def test_mapping(self):

        contour = np.array([
            [[10, 10]],
            [[10, 50]],
            [[60, 50]],
            [[60, 10]]
        ])

        mapper = ZoneMapper()

        zones = mapper.build([

            {
                "contour": contour,
                "risk": "Medium",
                "area": 2000
            }

        ])

        self.assertEqual(
            len(zones),
            1
        )

        self.assertEqual(
            zones[0]["risk"],
            "Medium"
        )


if __name__ == "__main__":
    unittest.main()
