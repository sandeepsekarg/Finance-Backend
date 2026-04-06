from fastapi import FastAPI
from app.database import engine, Base
from app.routes import record as record_routes
from app.routes import summary as summary_routes


# import models
from app.models import user, record

# import routes
from app.routes import user as user_routes

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# include routes
app.include_router(user_routes.router)

@app.get("/")
def home():
    return {"message": "Finance Backend Running 🚀"}

app.include_router(record_routes.router)
app.include_router(summary_routes.router)