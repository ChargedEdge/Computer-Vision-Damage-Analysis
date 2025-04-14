from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.api.endpoints import analyse_damage, retrieve_results, supported_materials, supported_types



app = FastAPI(
    title="Computer Vision Damage Analysis",
    description="API to detect damaged areas in images, identify affected materials, and classify damage type.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,     # Change if in production
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(supported_materials, prefix="/api/damage", tags=["Supported", "Materials"])
app.include_router(supported_types, prefix="/api/damage", tags=["Supported", "Damage"])

app.include_router(analyse_damage, prefix="/api/damage", tags=["Analysis"])
app.include_router(retrieve_results, prefix="/api/damage", tags=["Results"])