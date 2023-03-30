"""
--- UNITARY TESTS FOR DETECTOR-----------------------------------------------------------------------------------------
Fichero intencionado para probar la clase desarrollada como parte del proyecto mediante test unitarios.


Última edición: 30/03/2023
Autores: Blanca Rodríguez González (b.rodriguezg.2018@alumnos.urjc.es)
         Francisco C. Vázquez Donaire (fc.vazquez.2018@alumnos.urjc.es)

"""
import sys
sys.path.append('../../development/')


from BoundingBox import BoundingBox
from Detector import Detector
import cv2
import numpy as np
import unittest


class TestCarDetector(unittest.TestCase):
    def setUp(self):
        self.__detector = Detector((1024, 1024, 3), (512, 512, 3))

    def test_detect(self):
        image: np.array = np.array(cv2.imread("../../images/austin1.tif"))
        rectangles: list[BoundingBox] = self.__detector.detect(image)

        # Comprobruebo que se detectan coches, por lo que la funciona funciona correctamente, aunque la detección no sea muy precisa
        self.assertEqual(len(rectangles) > 10, True)


if __name__ == "__main__":
    unittest.main()
