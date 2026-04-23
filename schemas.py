from pydantic import BaseModel
from typing import List


class MovimientoBase(BaseModel):
    tipo: str
    monto: float
    cuenta_id: int


class MovimientoCreate(MovimientoBase):
    pass


class Movimiento(MovimientoBase):
    id: int

    class Config:
        from_attributes = True


class CuentaBase(BaseModel):
    saldo: float
    usuario_id: int


class CuentaCreate(CuentaBase):
    pass


class Cuenta(CuentaBase):
    id: int
    movimientos: List[Movimiento] = []

    class Config:
        from_attributes = True


class UsuarioBase(BaseModel):
    nombre: str
    correo: str


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int
    cuentas: List[Cuenta] = []

    class Config:
        from_attributes = True