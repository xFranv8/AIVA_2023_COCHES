"""
--- UNITARY TESTS FOR DETECTOR-----------------------------------------------------------------------------------------
Fichero intencionado para comprobar que la clase "Reader" es capaz de leer imagenes de forma correcta.

Última edición: 16/03/2023
Autores: Blanca Rodríguez González (b.rodriguezg.2018@alumnos.urjc.es)
         Francisco C. Vázquez Donaire (fc.vazquez.2018@alumnos.urjc.es)

"""
import sys
sys.path.append('../../development/')
from Reader import Reader
import numpy as np
import unittest


class TestReader(unittest.TestCase):
    def setUp(self):
        self.__image_path: str = "../../images/austin1.tif"

    def test_read_image(self):
        image: np.ndarray = Reader.read_image(self.__image_path)
        self.assertEqual(image.shape, (5000, 5000, 3))


if __name__ == "__main__":
    unittest.main()
