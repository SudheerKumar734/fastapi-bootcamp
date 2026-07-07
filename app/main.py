from fastapi import FastAPI
from app.routers import prediction
from app.exception_handler import global_exception_handler

app = FastAPI()

# Any unhandled exception will be caught by this handler
app.add_exception_handler(
    Exception, 
    global_exception_handler
)

app.include_router(
    prediction.router,
    prefix="/prediction",
    tags=["Prediction"]
)