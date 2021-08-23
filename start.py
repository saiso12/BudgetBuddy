import logging

import uvicorn

import os
# log datetime for each log message
log_config = logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__":
    # for key in sorted(os.environ.keys()):
    #     value = os.environ[key]
    #     print(f"key = {key}, value = {value}")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=5000,
        log_level="debug",
        reload=True,
        log_config=log_config,
    )
