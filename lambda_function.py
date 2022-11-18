from fastapi import FastAPI
from mangum import Mangum
import test

app = FastAPI(title='Category')


@app.get("/", tags=["default"])
async def get_root():
    return {"message": "Hello Vidhi"}


app.include_router(test.router)
lambda_handler = Mangum(app=app)
