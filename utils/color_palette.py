class ColorPalette:

    HEALTHY = (0, 180, 0)

    LOW_RISK = (0, 255, 255)

    MEDIUM_RISK = (0, 165, 255)

    HIGH_RISK = (0, 0, 255)

    BACKGROUND = (35, 35, 35)

    TEXT = (255, 255, 255)

    @classmethod
    def risk_color(cls, level):

        colors = {

            "Low": cls.LOW_RISK,

            "Medium": cls.MEDIUM_RISK,

            "High": cls.HIGH_RISK

        }

        return colors.get(level, cls.HEALTHY)
