from fastapi import FastAPI
from app.api.routes import router as chat_router
from app.frontend.routes import router as frontend_router
from fastapi.staticfiles import StaticFiles
app = FastAPI(
    title="WebQuery AI",
    version="1.0.0"
)
app.mount(
    "/static",
    StaticFiles(directory="app/frontend/static"),
    name="static"
)
app.include_router(frontend_router)
app.include_router(chat_router)
