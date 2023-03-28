import cv2
from Detector import Detector
import numpy as np
from BoundingBox import BoundingBox

SIZE = 125
def main():
    image: np.ndarray = cv2.imread("images/austin1.tif")
    detector: Detector = Detector((5000, 5000, 3), (SIZE, SIZE, 3))

    rectangles: list[BoundingBox] = detector.detect(image)

    
    for rectangle in rectangles:
        n: int = rectangle.patch_number

        print(f"Patch {n}")
        cv2.rectangle(image, (rectangle.point1[0]+(n%40)*SIZE, rectangle.point1[1]+(n//40)*SIZE), (rectangle.point2[0]+(n%40)*SIZE, rectangle.point2[1]+(n//40)*SIZE), (0, 255, 0), 2)

        """if rectangle.patch_number == 0:
            print(0)
            cv2.rectangle(image, rectangle.point1, rectangle.point2, (0, 255, 0), 2)
        elif rectangle.patch_number == 1:
            print(1)
            cv2.rectangle(image, (rectangle.point1[0]+SIZE, rectangle.point1[1]), (rectangle.point2[0]+SIZE, rectangle.point2[1]), (0, 255, 0), 2)
        elif rectangle.patch_number == 2:
            print(2)
            cv2.rectangle(image, (rectangle.point1[0]+ 2*SIZE, rectangle.point1[1]), (rectangle.point2[0]+2*SIZE, rectangle.point2[1]), (0, 255, 0), 2)
        elif rectangle.patch_number == 3:
            print(3)
            cv2.rectangle(image, (rectangle.point1[0]+ 3*SIZE, rectangle.point1[1]), (rectangle.point2[0]+3*SIZE, rectangle.point2[1]), (0, 255, 0), 2)
        elif rectangle.patch_number == 4:
            print(4)
            cv2.rectangle(image, (rectangle.point1[0]+ 4*SIZE, rectangle.point1[1]), (rectangle.point2[0]+4*SIZE, rectangle.point2[1]), (0, 255, 0), 2)
        elif rectangle.patch_number == 5:
            print(5)
            cv2.rectangle(image, (rectangle.point1[0]+ 5*SIZE, rectangle.point1[1]), (rectangle.point2[0]+5*SIZE, rectangle.point2[1]), (0, 255, 0), 2)
        elif rectangle.patch_number == 6:
            print(6)
            cv2.rectangle(image, (rectangle.point1[0]+ 6*SIZE, rectangle.point1[1]), (rectangle.point2[0]+6*SIZE, rectangle.point2[1]), (0, 255, 0), 2)
        elif rectangle.patch_number == 7:
            print(7)
            cv2.rectangle(image, (rectangle.point1[0]+ 7*SIZE, rectangle.point1[1]), (rectangle.point2[0]+7*SIZE, rectangle.point2[1]), (0, 255, 0), 2)"""
        """else:
            cv2.rectangle(image, (rectangle.point1[0]+SIZE, rectangle.point1[1]+SIZE), (rectangle.point2[0]+SIZE, rectangle.point2[1]+SIZE), (0, 255, 0), 3)"""
    
    cv2.imwrite("prueba.png", image)


if __name__ == "__main__":
    main()