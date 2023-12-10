from fastapi import FastAPI
import uvicorn

from routers import item, outlet, sale_report

app = FastAPI()

# router 
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(item.router)
app.include_router(outlet.router)
app.include_router(sale_report.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)