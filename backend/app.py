"""Main file for the backend."""

import logging

from litestar import Litestar
from litestar.logging import LoggingConfig
from server import routers
from server.database import close_database_connection_pool, open_database_connection_pool
from settings import ENVIRONMENT
from utils.middleware import cors_config, csrf_config

logging_config = LoggingConfig(
    root={"level": logging.getLevelName(logging.INFO), "handlers": ["console"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
)

# If the environment is development, enable debug mode
DEBUG_MODE = ENVIRONMENT == "development"


app = Litestar(
    cors_config=cors_config,
    csrf_config=csrf_config,
    route_handlers=routers.route_handlers,
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
    logging_config=logging_config,
    debug=DEBUG_MODE,
)
