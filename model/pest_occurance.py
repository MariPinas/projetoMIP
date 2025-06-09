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