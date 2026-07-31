from pathlib import Path

BASE_DIR = Path(__file__).parent

IMAGE_PATH = BASE_DIR / "data" / "sample_drone.jpg"

FIELD_METADATA = (
    BASE_DIR /
    "data" /
    "field_metadata.json"
)

OUTPUT_DIR = BASE_DIR / "output"

GAUSSIAN_KERNEL = (5, 5)

SEGMENTATION_THRESHOLD = 120

MIN_REGION_AREA = 250

HEALTHY_COLOR = (0, 200, 0)
DISEASE_COLOR = (0, 0, 255)

WINDOW_TITLE = "Crop Disease Detector"
