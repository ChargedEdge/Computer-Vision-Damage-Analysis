import json
from typing import List

class Results:
    def __init__(self, id: str, material: str, damages: List[str]):
        self.id = id
        self.material = material
        self.damages = damages

    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'material': self.material,
            'damages': self.damages
        })
    
    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(
            id = data['id'],
            material = data['material'],
            damages = data['damages']
        )