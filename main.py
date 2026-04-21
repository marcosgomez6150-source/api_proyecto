from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine
from models import Base

app = FastAPI(
    title="API de Billetera",
    description="Servicio web para la gestión de usuarios, cuentas y movimientos financieros",
    version="1.1.0"
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Inicio"])
def read_root():
    return {
        "mensaje": "API de la billetera funcionando correctamente en Render",
        "documentacion": "/docs",
        "redoc": "/redoc",
        "endpoints_disponibles": {
            "crear_usuario": "POST /usuarios/",
            "crear_cuenta": "POST /cuentas/",
            "ver_cuentas_usuario": "GET /usuarios/{usuario_id}/cuentas",
            "detalle_usuario": "GET /usuarios/{usuario_id}/detalle",
            "crear_movimiento": "POST /movimientos/",
            "ver_movimientos": "GET /movimientos/{cuenta_id}"
        }
    }


@app.post("/usuarios/", tags=["Usuarios"])
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)


@app.get("/usuarios/{usuario_id}/cuentas", tags=["Usuarios"])
def ver_cuentas_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(models.Cuenta).filter(models.Cuenta.usuario_id == usuario_id).all()

@app.get("/usuarios/{usuario_id}/detalle", tags=["Usuarios"])
def detalle_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    return usuario


@app.post("/cuentas/", tags=["Cuentas"])
def crear_cuenta(cuenta: schemas.CuentaCreate, db: Session = Depends(get_db)):
    return crud.crear_cuenta(db, cuenta)


@app.post("/movimientos/", tags=["Movimientos"])
def crear_movimiento(movimiento: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    return crud.crear_movimiento(db, movimiento)

@app.get("/movimientos/{cuenta_id}", tags=["Movimientos"])
def ver_movimientos(cuenta_id: int, db: Session = Depends(get_db)):
    return crud.obtener_movimientos(db, cuenta_id)