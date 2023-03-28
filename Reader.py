import cv2
import numpy as np


class Reader:
    @staticmethod
    def read_image(path: str) -> np.ndarray:
        return cv2.imread(path)


