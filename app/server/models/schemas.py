from pydantic import BaseModel
from uuid import UUID
from typing import List

# Response upon uploading image for analysis
class AnalysisSubmissionResponse(BaseModel):
    id: UUID
    status: str = "processing"
    message: str = "Your image is being analysed."


# Response upon retrieving using an ID
class AnalysisResultResponse(BaseModel):
    material: str
    damage_type: str



class DamageType(BaseModel):
    id: str
    name: str
    # description: str

class DamageTypesListResponse(BaseModel):
    damage_types: List[DamageType]




class MaterialType(BaseModel):
    id: str
    name: str
    # description: str

class MaterialTypesListResponse(BaseModel):
    materials: List[MaterialType]

