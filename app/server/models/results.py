import json
from typing import List, Literal

StatusType = Literal['processing', 'done', 'error']

class Results:
    def __init__(self, id: str, status: StatusType = 'processing', material: str = None, damages: List[str] = None):
        self.id = id
        self.material = material
        self.damages = damages
        self.status = status

    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'status': self.status,
            'material': self.material,
            'damages': self.damages
        })
    
    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(
            id = data['id'],
            status = data['status'],
            material = data['material'],
            damages = data['damages']
        )