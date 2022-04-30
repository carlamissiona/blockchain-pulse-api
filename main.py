from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request 
app = FastAPI()


# app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

templates = Jinja2Templates(directory="public")
foo = [{'image': 'Cassini', 'link': 'https://apod.nasa.gov/apod/image/1112/saturnstorm2_cassini_900.jpg', 'alt': 'A picture of UFO'},{'image': 'Cone Hubblesmidt', 'link': 'https://apod.nasa.gov/apod/image/1703/cone_hubbleschmidt_960.jpg', 'alt': 'A picture of UFO'},{'image': 'Jupiter Io Bianconi Collage', 'link': 'https://apod.nasa.gov/apod/image/1211/JupIoBianconiCollage.jpg', 'alt': 'A picture of UFO'},{'image': 'aaa', 'link': 'https://apod.nasa.gov/apod/image/9807/triple_jet.gif', 'alt': 'A picture of UFO'}, ]

# @app.get("/")
# def read_root():
#     return {"Hello": "Hello from FastAPI!"}

@app.get("/images/{item_id}")
def read_item(item_id: int, ):
    
    print(foo[item_id])    
    return {"item_id": item_id, "item": foo[item_id] }
  
@app.get("/images/")
def read_list(): 
    return {"items": foo }
  
@app.get("/")
async def home(request: Request):
   
   return templates.TemplateResponse("index.html",{"request":request, "images": foo })