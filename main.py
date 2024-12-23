from fastapi import FastAPI
import typing


app = FastAPI()

@app.get('/') 
async def read_root():
    data : dict[str,str] = {"massege":"Hello word"}
    return data


@app.get("/items/{item_id}")
async def read_item(item_id:int):
   data : dict[str , int] = {'massage': item_id}
   return data  



@app.get('/accounst/me')
async def me():
    data : dict[str , str] = {"username":"userdata"}
    return data