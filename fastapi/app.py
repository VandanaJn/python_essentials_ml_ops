from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Generate Date API",
        version="1.0.0",
        description="API to give date in the requested format",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


#to run locally
#uvicorn --host 0.0.0.0 app:app