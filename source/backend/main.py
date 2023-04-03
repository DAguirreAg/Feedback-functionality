from fastapi import FastAPI
import uvicorn
from config import Config
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sql_app import models
from feedback_management import feedback

# Main App
app = FastAPI(
    title=Config.TITLE,
    description=Config.DESCRIPTION,
    version=Config.VERSION,
    contact=Config.CONTACT,
    license_info=Config.LICENSE_INFO,
    openapi_tags=Config.TAGS_METADATA
)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5500"
    #"*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
models.Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(feedback.router)

if __name__ == "__main__":
    uvicorn.run(app, port=1234, host='0.0.0.0', reload=True)
