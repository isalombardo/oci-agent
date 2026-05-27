from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="OCI Agent")

class InvokeRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/invoke")
def invoke(req: InvokeRequest):
    return {
        "reply": f"Recebi sua mensagem: {req.message}"
    }
