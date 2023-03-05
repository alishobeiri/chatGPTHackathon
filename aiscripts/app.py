from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
import openai
from pydantic import BaseModel
openai.api_key = "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"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ApBioCurriculum")
async def home():
    APBioCurrculum = "prompt"
    try:
        answer = openai.Completion.create(engine="text-ada-001", prompt = APBioCurrculum, max_tokens=10).choices[0].text
    except:
        answer = "I am not sure what to say"
    return answer

@app.post("/")
def test(prompt: str):
    question = prompt
    try:
        answer = openai.Completion.create(engine="text-ada-001", prompt = question, max_tokens=10).choices[0].text
    except:
        answer = "I am not sure what to say"
    return answer
