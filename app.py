from core.image_loader import ImageLoader
from core.image_preprocessor import ImagePreprocessor
from core.vegetation_index import VegetationIndex
from core.disease_segmenter import DiseaseSegmenter
from visualization.dashboard import Dashboard


def main():

    loader = ImageLoader()

    image = loader.load()

    preprocessor = ImagePreprocessor()

    processed = preprocessor.process(image)

    vegetation = VegetationIndex()

    index = vegetation.calculate(processed)

    detector = DiseaseSegmenter()

    zones = detector.segment(index)

    dashboard = Dashboard()

    dashboard.show(image, zones)


if __name__ == "__main__":
    main()
