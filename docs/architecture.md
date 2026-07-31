# Architecture

```
                 app.py
                    │
                    ▼
             ImageLoader
                    │
                    ▼
         ImagePreprocessor
                    │
                    ▼
          VegetationIndex
                    │
                    ▼
         DiseaseSegmenter
                    │
                    ▼
         HealthClassifier
                    │
                    ▼
             ZoneMapper
          ┌─────────┴─────────┐
          ▼                   ▼
     ReportGenerator      Visualization
```

## Modules

- **ImageLoader** — loads drone images.
- **ImagePreprocessor** — applies image filtering.
- **VegetationIndex** — computes a vegetation index.
- **DiseaseSegmenter** — segments potentially diseased regions.
- **HealthClassifier** — assigns a severity level.
- **ZoneMapper** — converts contours into reportable zones.
- **ReportGenerator** — exports results to JSON.
- **Visualization** — renders overlays and heatmaps.
