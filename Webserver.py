from fastapi import FastAPI, HTTPException
from main import deploy_func

app = FastAPI()

@app.post("/post/")
async def post_videos(author: str):
    try:
        result = deploy_func(author, redirect_uris=["http://localhost"])
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))