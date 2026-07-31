import math


class Geometry:

    @staticmethod
    def rectangle_center(zone):

        return (

            zone["x"] + zone["width"] / 2,

            zone["y"] + zone["height"] / 2

        )

    @staticmethod
    def rectangle_area(zone):

        return zone["width"] * zone["height"]

    @staticmethod
    def distance(first, second):

        return math.sqrt(

            (first[0] - second[0]) ** 2 +

            (first[1] - second[1]) ** 2

        )
