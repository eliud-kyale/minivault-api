from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import ollama
import json

LOGFILE="logs/log.jsonl"
LLM_MODEL = 'llama3'

class Prompt(BaseModel):
    prompt: str

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""
    <html>
        <head>
            <title>Written by Eliud Kyale</title>
        </head>
        <body>
            <h1>MiniVault API using '{LLM_MODEL}' LLM local instance</h1>
        </body>
    </html>
    """

@app.post("/generate")
async def generate_response(prompt: Prompt):

    def log_data(data: list[dict]) -> None:
        with open(LOGFILE, "a") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")

    json_logs = []

    json_logs.append(prompt.model_dump())

    response = {
        'response': ''
    }
    for part in ollama.generate (model=LLM_MODEL,
                                 prompt=prompt.prompt,
                                 stream=True):
        response['response'] += part['response']
        print(part['response'], end='', flush=True)
    print('')
    json_logs.append(response)
    log_data(json_logs)
    return response
