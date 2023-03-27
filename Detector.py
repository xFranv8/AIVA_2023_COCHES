from BoundingBox import BoundingBox
import cv2
from ImagePatcher import ImagePatcher
import numpy as np
import pandas as pd
import torch


class Detector:
    def __init__(self, input_size: tuple, output_size: tuple) -> None:
        self.__model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.__patcher: ImagePatcher = ImagePatcher(input_size, output_size)


    def detect(self, image: np.ndarray) -> BoundingBox:
        subimages: list = self.__patcher.patch_image(image)

        i: int = 0
        bboxs: list = []
        for i in range(subimages.shape[0]):
            for j in range(subimages.shape[1]):
                img: np.ndarray = subimages[i, j, 0]

                results = self.__model(img)

                cv2.imshow("", img)
                if cv2.waitKey(0) == ord('c'):
                    continue

                dataframe: pandas.Dataframe = results.pandas().xyxy[0]
                # dataframe = dataframe[dataframe["class"] == 2]

                print(f"Image {i} \n Dataframe: {dataframe}")
        
                for row in dataframe.iterrows():
                    x1: int = row["xmin"]
                    y1: int = row["ymin"]

                    x2: int = row["xmax"]
                    y2: int = row["ymax"]

                    confidence: float = row["confidence"]

                    bbox: BoundingBox = BoundingBox((x1, y1), (x2, y2), confidence, i)
                    bboxs.append(bbox)

                i += 1
        
        return bboxs
        