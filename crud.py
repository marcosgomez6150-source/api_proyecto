def crear_usuario(db, usuario):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def crear_cuenta(db, cuenta):
    db_cuenta = models.Cuenta(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta


def crear_movimiento(db, movimiento):
    db_mov = models.Movimiento(**movimiento.dict())
    db.add(db_mov)
    db.commit()
    db.refresh(db_mov)
    return db_mov