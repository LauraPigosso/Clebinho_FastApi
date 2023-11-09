from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class CursoSchema(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str 
    horas: int
    aulas: int
    instrutor: str
    class Config:
        from_attributes = True