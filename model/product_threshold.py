from .pest import Pest

class ProductThreshold:
    def __init__ (self,
                  pest: Pest,
                  minimumOccurences: int,
                  dosePerHectare: float):
        self.pest = pest
        self.minimumOccurences = minimumOccurences
        self.dosePerHectare = dosePerHectare
    
    def is_applicable(self, occurrences: int) -> bool:
        return occurrences >= self.minimumOccurences

    def calculate_total_dose(self, area: float) -> float:
        return self.dosePerHectare * area
    