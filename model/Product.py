from typing import List
from uuid import UUID
from .product_threshold import ProductThreshold
from .pest import Pest

class Product:
    def __init__(self, 
                 product_id: UUID,
                 name: str,
                 costPerDose: float,
                 thresholds: List[ProductThreshold]):
        self.id = product_id
        self.name = name
        self.costPerDose = costPerDose
        self.thresholds = thresholds
        
    def get_threshold_for_pest(self, pest: Pest) -> 'ProductThreshold | None':
        for threshold in self.thresholds:
            if threshold.pest.name == pest.name:
                return threshold
        return None
                
        