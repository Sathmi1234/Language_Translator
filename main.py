from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from translator import translate_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.get("/")
def home():
    return {"message": "Translator Chatbot is running 🚀"}

@app.post("/translate")
def translate(req: TranslationRequest):
    result = translate_text(req.text, req.target_language)
    return {
        "bot_message": f"I translated it for you 😊",
        "translation": result["translated_text"]
    }
