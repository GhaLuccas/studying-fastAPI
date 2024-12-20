from fastapi import FastAPI
import typing


app = FastAPI()

@app.get('/') 
async def read_root():
    data : dict[str,str] = {"massege":"Hello word"}
    return data