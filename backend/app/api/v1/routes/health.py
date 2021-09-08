import logging
from fastapi import APIRouter

LOGGER = logging.getLogger()

router = APIRouter()


@router.get("/ping", tags=["HealthCheck"])
def pong():
    return {"ping": "pong"}