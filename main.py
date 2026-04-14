from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal, engine
from models import Base

app = FastAPI(
    title="API de Billetera",
    description="Servicio web para la gestión de usuarios, cuentas y movimientos financieros",
    version="1.0.0"
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Dependencia para la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Endpoint raíz
@app.get("/", tags=["Inicio"])
def read_root():
    return {
        "mensaje": "API de la billetera funcionando correctamente en Render",
        "documentacion": "/docs",
        "redoc": "/redoc",
        "endpoints_disponibles": {
            "crear_usuario": "POST /usuarios/",
            "crear_cuenta": "POST /cuentas/",
            "crear_movimiento": "POST /movimientos/",
            "ver_movimientos": "GET /movimientos/{cuenta_id}"
        }
    }

# Endpoint para crear un usuario
@app.post("/usuarios/", tags=["Usuarios"])
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

# Endpoint para crear una cuenta
@app.post("/cuentas/", tags=["Cuentas"])
def crear_cuenta(cuenta: schemas.CuentaCreate, db: Session = Depends(get_db)):
    return crud.crear_cuenta(db, cuenta)

# Endpoint para registrar un movimiento
@app.post("/movimientos/", tags=["Movimientos"])
def crear_movimiento(movimiento: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    return crud.crear_movimiento(db, movimiento)

# Endpoint para obtener los movimientos de una cuenta
@app.get("/movimientos/{cuenta_id}", tags=["Movimientos"])
def ver_movimientos(cuenta_id: int, db: Session = Depends(get_db)):
    return crud.obtener_movimientos(db, cuenta_id)