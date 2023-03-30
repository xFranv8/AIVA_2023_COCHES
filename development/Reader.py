import cv2
import numpy as np


class Reader:
    """
    Clase que contiene métodos estáticos para leer imágenes.
    """
    @staticmethod
    def read_image(path: str) -> np.ndarray:
        """
        Método estático que lee una imagen y la devuelve como un objeto numpy.ndarray. El argumento que recibe es
        - path: ruta de la imagen
        """
        
        return cv2.imread(path)


