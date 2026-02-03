import subprocess
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Command(BaseModel):
    cmd: str

def execute(cmd: str) -> str:
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
    output = execute(command.cmd)
    return {"output": output}
