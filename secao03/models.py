from typing import Optional

from pydantic import BaseModel



class curso(BaseModel):
    id: Optinal[int] = None
    titulo: str
    aulas: int
    horas: int