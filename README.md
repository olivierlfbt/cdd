# Crop Disease Detector

Crop Disease Detector is a Python application for detecting unhealthy crop areas from drone imagery.

The system processes aerial images, segments damaged vegetation, generates a health map, and highlights zones that may require inspection or treatment.

## Features

- Drone image processing
- Image preprocessing
- Disease segmentation
- Healthy vs unhealthy classification
- Vegetation analysis
- Problem zone mapping
- Heatmap generation
- JSON report export

## Project Structure

```
core/
visualization/
utils/
tests/
docs/
```

## Requirements

- Python 3.12+
- OpenCV
- NumPy
- Matplotlib

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## License

MIT
