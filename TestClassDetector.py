from CarDetector import CarDetector
import cv2
import numpy as np
import unittest


class TestCarDetector(unittest.TestCase):
    def setUp(self):
        self.car_detector = CarDetector((1024, 1024, 3), (512, 512, 3))

    def test_patcher(self):
        image: np.array = np.array(cv2.imread("test.png"))

        self.assertEqual(image.shape[0]/512, len(self.car_detector._patch_image(image)))

        reconstructered_images = self.car_detector._unpatch_image(self.car_detector._patch_image(image))

        self.assertEqual(True, (reconstructered_images == image).all())


if __name__ == "__main__":
    unittest.main()