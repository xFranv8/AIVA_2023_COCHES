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
