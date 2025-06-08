from typing import List
from uuid import UUID

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
        