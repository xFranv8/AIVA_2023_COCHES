from BoundingBox import BoundingBox
import cv2
from Detector import Detector
import numpy as np
from Reader import Reader
from ResultViewer import ResultViewer


SIZE = 125


def main():
    image: np.ndarray = Reader.read_image("Images/austin1.tif")
    detector: Detector = Detector((5000, 5000, 3), (SIZE, SIZE, 3))

    rectangles: list[BoundingBox] = detector.detect(image)
    ResultViewer.draw_results(image,rectangles)
    ResultViewer.write_csv(rectangles)



if __name__ == "__main__":
    main()
