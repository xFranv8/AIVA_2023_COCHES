from BoundingBox import BoundingBox
import cv2
from ImagePatcher import ImagePatcher
import numpy as np
import pandas as pd
from PIL import Image
import torch


class Detector:
    def __init__(self, input_size: tuple, output_size: tuple) -> None:
        self.__model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.__patcher: ImagePatcher = ImagePatcher(input_size, output_size)


    def detect(self, image: np.ndarray) -> BoundingBox:
        subimages: list = self.__patcher.patch_image(image)

        bboxs: list = []
        for i in range(subimages.shape[0]):
            for j in range(subimages.shape[1]):
                img: np.ndarray = np.array(Image.fromarray(subimages[i, j, 0]))

                
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                results = self.__model(img)

                dataframe: pd.Dataframe = results.pandas().xyxy[0]
                
                options: list = [2, 3, 5, 6, 7, 8]
                dataframe = dataframe[dataframe["class"].isin(options)]

                for index, row in dataframe.iterrows():
                    x1: int = int(row["xmin"])
                    y1: int = int(row["ymin"])

                    x2: int = int(row["xmax"])
                    y2: int = int(row["ymax"])

                    confidence: float = row["confidence"]

                    bbox: BoundingBox = BoundingBox((x1, y1), (x2, y2), confidence, i * subimages.shape[1] + j)
                    bboxs.append(bbox)
        
        return bboxs
        