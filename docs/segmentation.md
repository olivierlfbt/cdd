# Disease Segmentation

## Pipeline

```
Drone Image
      │
      ▼
Gaussian Blur
      │
      ▼
Vegetation Index
      │
      ▼
Threshold
      │
      ▼
Contour Detection
      │
      ▼
Region Classification
      │
      ▼
Problem Zone Map
```

## Processing Steps

1. Load RGB image.
2. Apply Gaussian filtering.
3. Compute vegetation index.
4. Normalize image values.
5. Segment unhealthy vegetation.
6. Remove very small regions.
7. Classify disease severity.
8. Export detected zones.
