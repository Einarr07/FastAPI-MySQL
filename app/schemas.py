from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    username: str
    nombre: str
    rol: str
    estado: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    nombre: str
    
    class Config:
        from_attributes = True

class Respuesta(BaseModel):
    mensaje: str
