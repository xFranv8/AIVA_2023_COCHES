from BoundingBox import BoundingBox
from Detector import Detector
import numpy as np
import os
from Reader import Reader
from ResultViewer import ResultViewer


class CarDensityAI:
    def __init__(self, image_path: str, size: int, output_path: str) -> None:
        if not os.path.exists(image_path):
            raise Exception("File not found.")
        
        self.__image: np.ndarray = Reader.read_image(image_path)
        self.__SIZE: int = size
        self.__detector = Detector(self.__image.shape, (self.__SIZE, self.__SIZE, 3))
        self.__output_path: str = output_path
    
    def main(self) -> None:
        rectangles: list[BoundingBox] = self.__detector.detect(self.__image)
        ResultViewer.draw_results(self.__image, rectangles, self.__SIZE, self.__output_path)
        ResultViewer.write_csv(rectangles, self.__output_path, self.__SIZE, self.__image.shape[0])


if __name__ == "__main__":
    cardensityai = CarDensityAI("../images/tyrol-w6.tif", 125, "tyrol-w6.csv")
    cardensityai.main()