class BoundingBox:
    def __init__(self, point1: tuple, point2: tuple, confidence: float, patch_number: int) -> None:
        self.point1 = point1
        self.point2 = point2
        self.confidence = confidence
        self.patch_number = patch_number
    
    def __str__(self) -> str:
        return str(self.point1) + ' ' + str(self.point2) + ' ' + str(self.patch_number) + ' ' + str(self.confidence)
        
    def __repr__(self) -> str:
        return str(self.point1) + ' ' + str(self.point2) + ' ' + str(self.patch_number) + ' ' + str(self.confidence)