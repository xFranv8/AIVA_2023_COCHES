"""
--- CARDENSITYAI-------------------------------------------------------------------------------------------------------
Fichero encargado de recoger el método para conteo y detección de vehículos.

Última edición: 16/03/2023
Autores: Blanca Rodríguez González (b.rodriguezg.2018@alumnos.urjc.es)
         Francisco C. Vázquez Donaire (fc.vazquez.2018@alumnos.urjc.es)
"""

import numpy as np
from patchify import patchify, unpatchify


class ImagePatcher:
    def __init__(self, original_shape: tuple, shape_patches: tuple):
        self.__original_shape: tuple = original_shape
        self.__patches_shape: tuple = shape_patches

    def __analyze_image(image: np.ndarray) -> list:
        """
        image: Subimagen en la que se va a realizar la detección 
        return list: Una lista conteniendo la imagen con los bbox dibujados y un vector con todas las coodernadas de los bbox relativas a esa subimagen
        """
        pass

    def patch_image(self, image: np.ndarray) -> list:
        """
        image: Imagen que se va a dividir 
        return list: Una lista conteniendo las subimagenes creadas
        """
        assert type(image) == np.ndarray

        return patchify(image, self.__patches_shape, step=self.__patches_shape[0])
    
    def unpatch_images(self, images: np.ndarray) -> np.ndarray:
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
