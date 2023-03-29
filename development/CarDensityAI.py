from BoundingBox import BoundingBox
from Detector import Detector
import numpy as np
import os
from Reader import Reader
from ResultViewer import ResultViewer


class CarDensityAI:
    def __init__(self, image_path: str, size: int) -> None:
        if not os.path.exists(image_path):
            raise Exception("File not found.")
        
        self.__image: np.ndarray = Reader.read_image(image_path)
        self.__SIZE: int = size
        self.__detector = Detector(self.__image.shape, (self.__SIZE, self.__SIZE, 3))
    
    def main(self) -> None:
        rectangles: list[BoundingBox] = self.__detector.detect(self.__image)
        ResultViewer.draw_results(self.__image, rectangles, self.__SIZE)
        ResultViewer.write_csv(rectangles)


if __name__ == "__main__":
    cardensityai = CarDensityAI("../images/chicago1.tif", 250)
    cardensityai.main()