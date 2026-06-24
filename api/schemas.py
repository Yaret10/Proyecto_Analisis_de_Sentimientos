from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    model: str
    text: str
    label: str
    score: float
