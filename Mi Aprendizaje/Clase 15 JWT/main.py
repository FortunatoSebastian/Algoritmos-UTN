from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import iniciar_db, get_conexion
from auth import encriptar_password, verificar_password, crear_token, verificar_token
from pydantic import BaseModel

app = FastAPI(BaseModel)
iniciar_db()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class Usuario(BaseModel):
    username: str
    pssword: str
    
# Registro

@app.post("/registro")
def registro(usuario: Usuario):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (usuario.username,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    password_hash = encriptar_password(usuario.password)
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (usuario.username, password_hash))
    conexion.commit()
    conexion.close()
    return {"mensaje": "Usuario Registrado Correctamente"}

# LOGIN

@app.post("/login")
def login(form:OAuth2PasswordRequestForm = Depends()):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (form.username))
    usuario = cursor.fetchone()
    conexion.close()
    if not usuario or not verificar_password(form.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = crear_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

# ruta protegida

@app.get("/perfil")
def perfil(token: str = Depends(oauth2_scheme)):
    username = verificar_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Token invalido")
    return {"mensaje": f"Bienvenido {username}"}