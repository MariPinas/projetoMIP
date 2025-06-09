from uuid import UUID
from typing import Optional
from .pest_occurrence import PestOccurrence

class Region:
    def __init__(self,
                 region_id: UUID,
                 name: str,
                 size: float,
                 parentRegion: Optional['Region'] = None):
        self.id = region_id
        self.name = name
        self.size = size
        self.parentRegion = parentRegion
        
    def get_full_name(self) -> str:
        if self.parentRegion:
            return f"{self.parentRegion.get_full_name()} > {self.name}"
        return self.name

    def get_size(self) -> float:
        return self.size

    def contains_occurrence(self, occurrence: PestOccurrence) -> bool:
        return occurrence.region.id == self.id    