from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Dict

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/api/v1/health", summary="Health check", description="Check if the API is up.")
async def get_health_check_status() -> Dict:
    """Generate a health check response for the applications."""
    return {"status": "UP", "details": "Application is running normally."}

@app.get("/home",include_in_schema=False, response_class=HTMLResponse)
async def main(request: Request):
    """Render index page into root endpoint."""
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    print('main function called')