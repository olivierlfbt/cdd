import json
from pathlib import Path
from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.output = Path("output")

        self.output.mkdir(
            exist_ok=True
        )

    def save(self, zones):

        report = {

            "generatedAt":
                datetime.now().isoformat(),

            "problemZones":
                len(zones),

            "zones":
                zones

        }

        file = self.output / "crop_report.json"

        with open(file, "w") as fp:

            json.dump(
                report,
                fp,
                indent=4
            )

        return file
