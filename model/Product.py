from typing import List
from uuid import UUID
from .product_threshold import ProductThreshold
from .pest import Pest

class Product:
    def __init__(self, 
                 product_id: UUID,
                 name: str,
                 cost_per_dose: float,
                 thresholds: List[ProductThreshold]):
        self.id = product_id
        self.name = name
        self.cost_per_dose = cost_per_dose
        self.thresholds = thresholds
        
    def get_threshold_for_pest(self, pest: Pest) -> 'ProductThreshold | None':
        for threshold in self.thresholds:
            if threshold.pest.name == pest.name:
                return threshold
        return None
    
    def should_apply(self, pest: Pest, occurrences: int) -> bool:
        threshold = self.get_threshold_for_pest(pest)
        if threshold and threshold.is_applicable(occurrences):
            return True
        return False

    def calculate_dose(self, pest: Pest, occurrences: int, area: float) -> float:
        threshold = self.get_threshold_for_pest(pest)
        if threshold:
            return threshold.calculate_total_dose(area)
        return 0.0

    def calculate_cost(self, pest: Pest, occurrences: int, area: float) -> float:
        doses = self.calculate_dose(pest, occurrences, area)
        return doses * self.cost_per_dose

