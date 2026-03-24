from sqlalchemy.orm import Session
import models

def crear_usuario(db: Session, usuario):
    nuevo = models.Usuario(nombre=usuario.nombre)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def crear_cuenta(db: Session, cuenta):
    nueva = models.Cuenta(banco=cuenta.banco, usuario_id=cuenta.usuario_id)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def crear_movimiento(db: Session, movimiento):
    cuenta = db.query(models.Cuenta).filter(models.Cuenta.id == movimiento.cuenta_id).first()
    
    if movimiento.tipo == "deposito":
        cuenta.saldo += movimiento.monto
    elif movimiento.tipo == "retiro":
        cuenta.saldo -= movimiento.monto

    nuevo = models.Movimiento(**movimiento.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_movimientos(db: Session, cuenta_id: int):
    return db.query(models.Movimiento).filter(models.Movimiento.cuenta_id == cuenta_id).all()