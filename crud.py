from sqlalchemy.orm import Session
import models
import schemas


# 🔹 CREAR USUARIO
def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# 🔹 CREAR CUENTA
def crear_cuenta(db: Session, cuenta: schemas.CuentaCreate):
    db_cuenta = models.Cuenta(
        saldo=cuenta.saldo,
        usuario_id=cuenta.usuario_id
    )
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta


# 🔹 CREAR MOVIMIENTO
def crear_movimiento(db: Session, movimiento: schemas.MovimientoCreate):
    db_mov = models.Movimiento(
        tipo=movimiento.tipo,
        monto=movimiento.monto,
        cuenta_id=movimiento.cuenta_id
    )
    db.add(db_mov)
    db.commit()
    db.refresh(db_mov)
    return db_mov