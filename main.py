from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
app = FastAPI()


app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

templates = Jinja2Templates(directory="public")


# @app.get("/")
# def read_root():
#     return {"Hello": "Hello from FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}
  
@app.get("/")
async def home(request: Request):
   
   return templates.TemplateResponse("index.html",{"request":request})