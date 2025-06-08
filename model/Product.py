from typing import List
from uuid import UUID

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
        