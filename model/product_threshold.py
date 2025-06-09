from .pest import Pest

class ProductThreshold:
    def __init__ (self,
                  pest: Pest,
                  minimumOccurences: int,
                  dosePerHectare: float):
        self.pest = pest
        self.minimumOccurences = minimumOccurences
        self.dosePerHectare = dosePerHectare