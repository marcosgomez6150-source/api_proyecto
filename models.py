from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

class Cuenta(Base):
    __tablename__ = "cuentas"
    id = Column(Integer, primary_key=True, index=True)
    banco = Column(String)
    saldo = Column(Float, default=0)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)  # deposito o retiro
    monto = Column(Float)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"))