import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")

# Generic Api related configs
API_V1_PREFIX = "/api/v1"
API_NAME = "BudgetBuddy"
API_DESCRIPTION = "Spending tracker and your Budget Buddy"


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DB_URL")


# using the caching decorator to minimize the load time
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading Config settings from the env...")
    return Settings()
