from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

FAKE_USER = "admin"
FAKE_PASSWORD = "123456"
API_TOKEN = "mi_token_secreto"


def login_user(username: str, password: str):
    if username == FAKE_USER and password == FAKE_PASSWORD:
        return API_TOKEN

    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    if token != API_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    return True
