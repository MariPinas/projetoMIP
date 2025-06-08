from uuid import UUID

class Region:
    def __init__(self,
                 region_id: UUID,
                 name: str,
                 size: float,
                 parentRegion: Region,
                 size: float):
        self.id = region_id
        self.name = name
        self.size = size
        self.parentRegion = parentRegion