from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request 
app = FastAPI()


# app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

templates = Jinja2Templates(directory="public")
foo = [{'image': 'aaa', 'link': 'bbb', 'alt': 'A picture of UFO'},{'image': 'aaa', 'link': 'bbb', 'alt': 'A picture of UFO'}, ]

# @app.get("/")
# def read_root():
#     return {"Hello": "Hello from FastAPI!"}

@app.get("/images/{item_id}")
def read_item(item_id: int, ):
    
    print(foo[item_id])    
    return {"item_id": item_id }
  
@app.get("/")
async def home(request: Request):
   
   return templates.TemplateResponse("index.html",{"request":request})