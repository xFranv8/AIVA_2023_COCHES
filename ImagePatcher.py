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

