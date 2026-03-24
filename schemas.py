from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str

class CuentaCreate(BaseModel):
    banco: str
    usuario_id: int

class MovimientoCreate(BaseModel):
    tipo: str
    monto: float
    cuenta_id: int