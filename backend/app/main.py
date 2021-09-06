import logging

from fastapi import FastAPI


from app.api.v1.routes import health, imageProcessor
from app.config import (
    API_DESCRIPTION,
    API_NAME,
    API_V1_PREFIX,
)

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(health.router, prefix=API_V1_PREFIX)
    application.include_router(imageProcessor.router, prefix=API_V1_PREFIX)
    return application


# invoke method to create FastAPI object , which inturn runs the uvicorn server
app = create_application()


# TODO: DB init must go here!
@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
