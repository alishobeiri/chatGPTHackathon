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

@app.get("/Ap-Bio-Curriculum")
def home():
    try:
        answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a system that generates questions based only on the following curriculum: ${ApBioCurriculum}"},
                {"role": "user", "content": "Provide 5 multiple choice questions for AP biology in a JSON format: { questions: [ question: <question>, choices: [<choice>, <choice>], correct_choice: <correct choice>, answer: <answer in the form of a sentence> ], ... }"},
            ])
        print(answer)
    except Exception as e:
        print(e)
        answer = e
    return answer

@app.post("/")
def test(prompt: str):
    question = prompt
    try:
        answer = openai.ChatCompletion.create(engine="gpt-3.5-turbo", prompt = question, max_tokens=10).choices[0].text
    except:
        answer = "I am not sure what to say"
    return answer

ApBioCurriculum = """
    Unit 1: Chemistry of Life 8–11% 
    Unit 2: Cell Structure and Function 10–13% 
    Unit 3: Cellular Energetics 12–16% 
    Unit 4: Cell Communication and Cell Cycle 10–15% 
    Unit 5: Heredity 8–11% 
    Unit 6: Gene Expression and Regulation 12–16% 
    Unit 7: Natural Selection 13–20% 
    Unit 8: Ecology 10–15%"""