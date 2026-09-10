
from pydantic import BaseModel, Field

from datetime import date

class RegistroHistorico(BaseModel):
    
    fecha: date
    
    unidades: float = Field(ge=0,description="Unidades vendidos ese dia, no puede ser negativo")

class SolicitudPronostico(BaseModel):
        store: int = Field(ge=1,le=10,description="El número de tiendas, del 1 al 10")
        item: int = Field(ge=1,le=50,description="El número de producto,del 1 al 50")
        
        historial: list[RegistroHistorico] = Field(min_length=28,max_length=365,
                                                   description="Histórico reciente de la serie. Mínimo 28 registros")
        
        
        horizonte: int = Field(default=14,ge=1,le=28,description="Días a pronosticar, de 1 a 28")
