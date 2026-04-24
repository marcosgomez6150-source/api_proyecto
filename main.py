from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine

# 🔥 OPCIÓN 2: RESETEAR BASE DE DATOS
models.Base.metadata.drop_all(bind=engine)     # BORRA tablas
models.Base.metadata.create_all(bind=engine)   # CREA tablas nuevas

app = FastAPI(
    title="API de Billetera",
    description="Servicio web para la gestión de usuarios, cuentas y movimientos financieros",
    version="1.1.0"
)

# 🔹 Conexión a BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Endpoint raíz
@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente"}

# 🔹 Usuarios
@app.post("/usuarios/")
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

# 🔹 Cuentas
@app.post("/cuentas/")
def crear_cuenta(cuenta: schemas.CuentaCreate, db: Session = Depends(get_db)):
    return crud.crear_cuenta(db, cuenta)

# 🔹 Movimientos
@app.post("/movimientos/")
def crear_movimiento(movimiento: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    return crud.crear_movimiento(db, movimiento)

@app.get("/movimientos/{cuenta_id}")
def ver_movimientos(cuenta_id: int, db: Session = Depends(get_db)):
    return crud.obtener_movimientos(db, cuenta_id)