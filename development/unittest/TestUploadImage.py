"""
--- UNITARY TESTS FOR UPLOADING IMAGES VIA HTTP METHODS-----------------------------------------------------------------------------------------
Fichero intencionado para comprobar que la subida de imágenes mediante HTTP funciona correctamente.


Última edición: 30/03/2023
Autores: Blanca Rodríguez González (b.rodriguezg.2018@alumnos.urjc.es)
         Francisco C. Vázquez Donaire (fc.vazquez.2018@alumnos.urjc.es)

"""

import os
import requests
import unittest


class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/upload/'
        self.image_path = 'test.png'

    def test_upload_image(self):
        response = requests.get(self.url)
        cookies = response.cookies

        with open(self.image_path, 'rb') as f:
            image_data = f.read()

        data = {
            'image': ('image.jpg', image_data)
            }
        

        header = {
            'X-CSRFToken': cookies["csrftoken"]
            }
        
        response = requests.post(self.url, files=data, cookies=cookies, headers=header)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Imagen guardada correctamente", response.text)

    def tearDown(self):
        os.remove('WebApplication/imagen.png')


if __name__ == '__main__':
    unittest.main()
