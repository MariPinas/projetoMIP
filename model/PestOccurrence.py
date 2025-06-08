from uuid import UUID
from datetime import datetime
from typing import Tuple
from model.Region import Region
from model.Pest import Pest

class PestOccurrence:
    def __init__(self,
                 occurrence_id: UUID,
                 region: Region,
                 pest: Pest,
                 createdAt: datetime,
                 location : Tuple[float, float]):
        self.id = occurrence_id
        self.region = region
        self.pest = pest
        self.createdAt = createdAt
        self.location = location