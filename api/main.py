from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from api.schemas import LoginRequest, TokenResponse, SentimentRequest, SentimentResponse
from api.auth import login_user, verify_token
from api.model_service import predict_base, predict_finetuned

app = FastAPI(
    title="API de Análisis de Sentimientos",
    description="API para comparar RoBERTuito base vs RoBERTuito fine-tuned",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="web"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#@app.get("/")
#def home():
#    return {
#        "message": "API de análisis de sentimientos funcionando"
#    }


@app.get("/")
def home():
    return FileResponse("web/login.html")


@app.get("/login.html")
def login_page():
    return FileResponse("web/login.html")


@app.get("/index.html")
def index_page():
    return FileResponse("web/index.html")


@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    token = login_user(request.username, request.password)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.post("/predict/base", response_model=SentimentResponse)
def predict_with_base(
    request: SentimentRequest,
    authenticated: bool = Depends(verify_token)
):
    return predict_base(request.text)


@app.post("/predict/finetuned", response_model=SentimentResponse)
def predict_with_finetuned(
    request: SentimentRequest,
    authenticated: bool = Depends(verify_token)
):
    return predict_finetuned(request.text)


@app.post("/predict/compare")
def compare_models(
    request: SentimentRequest,
    authenticated: bool = Depends(verify_token)
):
    return {
        "text": request.text,
        "base_model": predict_base(request.text),
        "finetuned_model": predict_finetuned(request.text)
    }
