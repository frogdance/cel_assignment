from fastapi import FastAPI
from routers import item, outlet, sale_report

app = FastAPI()

# router 
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(item.router)
app.include_router(outlet.router)
app.include_router(sale_report.router)