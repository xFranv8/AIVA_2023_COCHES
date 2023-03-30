class BoundingBox:
    """
    Clase que representa un bounding box.
    """
    def __init__(self, point1: tuple, point2: tuple, confidence: float, patch_number: int) -> None:
        """
        Constructor de la clase BoundingBox. Recibe como argumentos
        - point1: tupla que contiene las coordenadas del punto superior izquierdo del bounding box
        - point2: tupla que contiene las coordenadas del punto inferior derecho del bounding box
        - confidence: confianza de la predicción
        - patch_number: número del parche en el que se encuentra el bounding box
        """
        
        self.point1 = point1
        self.point2 = point2
        self.confidence = confidence
        self.patch_number = patch_number
    
    def __str__(self) -> str:
        return str(self.point1) + ' ' + str(self.point2) + ' ' + str(self.patch_number) + ' ' + str(self.confidence)
        
    def __repr__(self) -> str:
        return str(self.point1) + ' ' + str(self.point2) + ' ' + str(self.patch_number) + ' ' + str(self.confidence)