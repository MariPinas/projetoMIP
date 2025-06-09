from .pest import Pest

class ProductThreshold:
    def __init__ (self,
                  pest: Pest,
                  minimum_occurrence: int,
                  dose_per_hectare: float):
        self.pest = pest
        self.minimum_occurrence = minimum_occurrence
        self.dose_per_hectare = dose_per_hectare
    
    def is_applicable(self, occurrences: int) -> bool:
        return occurrences >= self.minimum_occurrence

    def calculate_total_dose(self, area: float) -> float:
        return self.dose_per_hectare * area
    