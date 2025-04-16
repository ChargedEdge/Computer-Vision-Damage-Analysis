from pydantic import BaseModel
from uuid import UUID
from typing import List
from typing_extensions import Literal

from app.definitions import SUPPORTED_MATERIALS, SUPPORTED_MATERIAL_DAMAGES


MaterialID = Literal.__getitem__(tuple(SUPPORTED_MATERIALS))


# Response upon uploading image for analysis
class AnalysisSubmissionResponse(BaseModel):
    id: UUID
    status: str = "processing"
    message: str = "Your image is being analysed."


# Response upon retrieving using an ID
class AnalysisResultResponse(BaseModel):
    material: str
    damage_type: list[str]


