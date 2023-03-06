import cv2
import numpy as np
from patchify import patchify, unpatchify


class CarDetector:
    def __init__(self, original_shape: tuple, shape_patches: tuple):
        self.__original_shape = original_shape
        self.__patches_shape: tuple = shape_patches

    def __analyze_image(image: np.ndarray) -> list:
        """
        image: Subimagen en la que se va a realizar la detección 
        return list: Una lista conteniendo la imagen con los bbox dibujados y un vector con todas las coodernadas de los bbox relativas a esa subimagen
        """
        pass

    def _patch_image(self, image: np.ndarray) -> list:
        """
        image: Imagen que se va a dividir 
        return list: Una lista conteniendo las subimagenes creadas
        """
        assert type(image) == np.ndarray

        return patchify(image, self.__patches_shape, step=self.__patches_shape[0])
    
    def _unpatch_image(self, images: np.ndarray) -> np.ndarray:
        """
        images: Lista conteniendo las subimagenes
        return ndarray: Imagen original
        """
        assert type(images) == np.ndarray

        return unpatchify(images, self.__original_shape)

    def detect_cars(self, image: str) -> list:
        """
        image: Imagen en la que se va a realizar la detección 
        list: Una lista conteniendo la imagen con los bbox dibujados y un vector con todas las coodernadas de los bbox en coordenadas absolutas
        """
        pass