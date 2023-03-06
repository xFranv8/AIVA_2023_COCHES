import cv2
from django.shortcuts import render
import numpy as np

# Create your views here.

def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        # Guardar la imagen en el servidor
        image = request.FILES['image']
        image_data = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite('imagen.png', image_data)
        
        return render(request, 'upload.html', {'success': True})
    return render(request, 'upload.html')
