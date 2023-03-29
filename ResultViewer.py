from BoundingBox import BoundingBox
import cv2
import csv
import numpy as np

class ResultViewer:
    @staticmethod
    def counter(rectangles: list[BoundingBox]):
        return len(rectangles)

    @staticmethod
    def draw_results(image: np.ndarray, rectangles: list[BoundingBox], SIZE: int):
        for rectangle in rectangles:
            n: int = rectangle.patch_number
            length: int = image.shape[0]

            cv2.rectangle(image, (rectangle.point1[0] + (n % (length//SIZE)) * SIZE, rectangle.point1[1] + (n // (length//SIZE)) * SIZE),
                          (rectangle.point2[0] + (n % (length//SIZE)) * SIZE, rectangle.point2[1] + (n // (length//SIZE)) * SIZE), (0, 255, 0), 1)

        cv2.imwrite("detection.png", image)

        aux = cv2.waitKey(0)

    @staticmethod
    def write_csv(rectangles: list[BoundingBox]):
        cars_count = ResultViewer.counter(rectangles)
        cars_detected = ['Cars detected', cars_count]
        filename = 'my_file.csv'

        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(cars_detected)

            for rectangle in rectangles:
                writer.writerow([rectangle.point1[0], rectangle.point1[1]])

        print(f"{filename} has been created successfully!")
