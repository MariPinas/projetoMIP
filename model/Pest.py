from uuid import UUID

class Pest:
    def __init__(self,
                 pest_id: UUID,
                 name: str):
        self.id = pest_id
        self.name = name
    
    def __str__(self):
        return f"Pest: {self.name}"