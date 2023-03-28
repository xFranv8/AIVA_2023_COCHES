from BoundingBox import BoundingBox
import cv2
import csv
import numpy as np

class ResultViewer:
    @staticmethod
    def counter(rectangles:list[BoundingBox]):
        return len(rectangles)

    @staticmethod
    def draw_results(image:np.array,rectangles:list[BoundingBox],SIZE:int):
        for rectangle in rectangles:
            n: int = rectangle.patch_number
            cv2.rectangle(image, (rectangle.point1[0] + (n % 40) * SIZE, rectangle.point1[1] + (n // 40) * SIZE),
                          (rectangle.point2[0] + (n % 40) * SIZE, rectangle.point2[1] + (n // 40) * SIZE), (0, 255, 0), 2)

        cv2.imshow(image)

        aux = cv2.waitKey(0)

    @staticmethod
    def write_csv(rectangles:list[BoundingBox]):
        cars_count = ResultViewer.counter(rectangles)
        cars_detected= ['Cars detected', cars_count]
        filename = 'my_file.csv'

        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(cars_detected)
            writer.writerow('BBox')


            for rectangle in rectangles:
                writer.writerow([rectangle.point1[0],rectangle.point1[1]])

        print(f"{filename} has been created successfully!")
