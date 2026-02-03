import subprocess
import json
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Pydantic modeli – HTTP POST orqali keladigan JSON uchun
class Command(BaseModel):
    cmd: str

def execute(cmd: str) -> str:
    """Buyruqni bajarib, natijasini qaytaradi"""
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output.decode()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/exec")
def run_command(command: Command):
    """HTTP POST orqali kelgan buyruqni bajaradi"""
    output = execute(command.cmd)
    return {"output": output}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
