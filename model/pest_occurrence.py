from uuid import UUID
from datetime import datetime
from typing import Tuple
from typing import Optional
from .pest import Pest

class PestOccurrence:
    def __init__(self,
                 occurrence_id: UUID,
                 pest: Pest,
                 createdAt: datetime,
                 location : Tuple[float, float],
                 region: Optional['Region'] = None):
        self.id = occurrence_id
        self.region = region
        self.pest = pest
        self.createdAt = createdAt
        self.location = location
    
    def get_occurrence_info(self) -> str:
        return (f"[{self.createdAt.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"Praga: {self.pest.name}, Região: {self.region.name if self.region else 'Indefinida'}, "
                f"Localização: ({self.location[0]}, {self.location[1]})")

    def matches_pest(self, pest: Pest) -> bool:
        return self.pest.id == pest.id