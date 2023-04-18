import sys
sys.path.append("../../")
sys.path.append("..")


import cv2
from development.CarDensityAI import CarDensityAI
from django.shortcuts import render
import numpy as np
import os

# Create your views here.

def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        # Guardar la imagen en el servidor
        image = request.FILES['image']
        image_data = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

        if not os.path.exists("results/"):
            os.makedirs("results/")

        cv2.imwrite("results/imagen.png", image_data)

        cardensityai = CarDensityAI("results/imagen.png", 125, "results/recuento_coches.csv")
        cardensityai.main()
        
        return render(request, 'upload.html', {'success': True})
        
    return render(request, 'upload.html')