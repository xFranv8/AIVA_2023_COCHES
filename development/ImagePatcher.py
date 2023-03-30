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
    """
    Clase que contiene métodos para dividir una imagen en subimagenes y para unir las subimagenes en una imagen original. 
    """
    def __init__(self, original_shape: tuple, shape_patches: tuple):
        """
        Constructor de la clase ImagePatcher. Recibe como argumentos
        - original_shape: tupla que contiene las dimensiones de la imagen original
        - shape_patches: tupla que contiene las dimensiones de las subimagenes
        """
        
        self.__original_shape: tuple = original_shape
        self.__patches_shape: tuple = shape_patches

    def patch_image(self, image: np.ndarray) -> list:
        """
        Método que divide una imagen en subimagenes. Recibe como argumento
        - image: imagen original
        """

        assert type(image) == np.ndarray

        return patchify(image, self.__patches_shape, step=self.__patches_shape[0])
    
    def unpatch_images(self, images: np.ndarray) -> np.ndarray:
        """
        Método que une las subimagenes en una imagen original. Recibe como argumento
        - images: subimágenes
        """

        assert type(images) == np.ndarray

        return unpatchify(images, self.__original_shape)

