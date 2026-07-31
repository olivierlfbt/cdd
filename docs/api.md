# Internal API

## ImageLoader

### load()

Returns an OpenCV image.

---

## ImagePreprocessor

### process(image)

Returns a filtered image.

---

## VegetationIndex

### calculate(image)

Returns a vegetation index matrix.

---

## DiseaseSegmenter

### segment(index)

Returns detected contours.

---

## HealthClassifier

### classify(contours)

Returns classified disease regions.

---

## ZoneMapper

### build(image, regions)

Returns mapped problem zones.

---

## ReportGenerator

### save(zones)

Creates a JSON report.
