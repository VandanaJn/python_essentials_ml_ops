from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Serve static HTML file
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Define request body schema
class Body(BaseModel):
    strftime: str | None = None

# Generate timestamp based on template
@app.post("/generate")
def generate(body: Body):
    """
    Generate the current time given a strftime template.
    For example: '%Y-%m-%dT%H:%M:%S.%f'
    """
    tmpl = body.strftime or "%Y-%m-%dT%H:%M:%S.%f"
    return {"date": datetime.now().strftime(tmpl)}

#to run locally
#uvicorn --host 0.0.0.0 app:app