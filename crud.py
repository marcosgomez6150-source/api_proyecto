from sqlalchemy.orm import Session
import models
import schemas


def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def crear_cuenta(db: Session, cuenta: schemas.CuentaCreate):
    db_cuenta = models.Cuenta(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta


def crear_movimiento(db: Session, movimiento: schemas.MovimientoCreate):
    db_mov = models.Movimiento(**movimiento.dict())
    db.add(db_mov)
    db.commit()
    db.refresh(db_mov)
    return db_mov


def obtener_movimientos(db: Session, cuenta_id: int):
    return db.query(models.Movimiento).filter(
        models.Movimiento.cuenta_id == cuenta_id
    ).all()