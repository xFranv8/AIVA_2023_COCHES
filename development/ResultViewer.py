from BoundingBox import BoundingBox
import cv2
import csv
import numpy as np


class ResultViewer:
    """
    Clase que contiene métodos estáticos para dibujar los resultados de la detección de coches en una imagen y para escribir los resultados en un fichero .csv. 
    """
    @staticmethod
    def counter(rectangles: list[BoundingBox]):
        """
        Método estático que cuenta el número de coches detectados en una imagen.
        """

        return len(rectangles)

    @staticmethod
    def draw_results(image: np.ndarray, rectangles: list[BoundingBox], SIZE: int, output_path: str):
        """
        Método estático que dibuja los rectángulos de los coches detectados en una imagen.  Además, guarda la imagen en un fichero .png.
        Los argumentos que recibe son
        - image: imagen en la que se dibujarán los rectángulos
        - rectangles: lista de objetos BoundingBox que contienen la información de los rectángulos a dibujar
        - SIZE: tamaño de los parches en los que se divide la imagen
        - output_path: ruta del fichero en el que se guardará la imagen
        """
        
        LENGTH: int = image.shape[0]
        for rectangle in rectangles:
            n: int = rectangle.patch_number

            cv2.rectangle(image, (ResultViewer.__local_to_global(rectangle.point1, n, SIZE, LENGTH)), (ResultViewer.__local_to_global(rectangle.point2, n, SIZE, LENGTH)), (0, 255, 0), 1)

        cv2.imwrite(f"{output_path.split('.')[0]}.png", image)

        aux = cv2.waitKey(0)

    @staticmethod
    def write_csv(rectangles: list[BoundingBox], output_path: str, SIZE: int, LENGTH: int):
        """
        Método estático que escribe los resultados de la detección de coches en un fichero .csv. Los argumentos que recibe son
        - rectangles: lista de objetos BoundingBox que contienen la información de los rectángulos a dibujar
        - output_path: ruta del fichero en el que se guardará la imagen
        - SIZE: tamaño de los parches en los que se divide la imagen
        - LENGTH: longitud de la imagen
        """

        cars_count = ResultViewer.counter(rectangles)
        cars_detected = ['Cars detected', cars_count]

        filename: str = output_path.split('.')[0] + ".csv"

        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(cars_detected)

            for rectangle in rectangles:
                n: int = rectangle.patch_number
                pt1: tuple[int, int] = ResultViewer.__local_to_global(rectangle.point1, n, SIZE, LENGTH)
                pt2: tuple[int, int] = ResultViewer.__local_to_global(rectangle.point2, n, SIZE, LENGTH)

                writer.writerow([pt1[0], pt1[1], pt2[0], pt2[1]])

        print(f"{filename} has been created successfully!")
    
    @staticmethod
    def __local_to_global(point: tuple[int, int], patch_number: int, SIZE: int, length: int):
        """
        Método estático que convierte las coordenadas locales de un punto a coordenadas globales. Los argumentos que recibe son
        - point: tupla de dos enteros que contiene las coordenadas locales del punto
        - patch_number: número del parche en el que se encuentra el punto
        - SIZE: tamaño de los parches en los que se divide la imagen
        - length: longitud de la imagen
        """
        return point[0] + (patch_number % (length//SIZE)) * SIZE, point[1] + (patch_number // (length//SIZE)) * SIZE
