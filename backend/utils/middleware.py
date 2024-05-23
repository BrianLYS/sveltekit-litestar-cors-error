"""Middleware for the application."""

from litestar.config.cors import CORSConfig
from litestar.config.csrf import CSRFConfig
from settings import SECRET_KEY

# CSRF
csrf_config = CSRFConfig(
    secret=str(SECRET_KEY),
    safe_methods={
        "GET",
        "POST",
        "DELETE",
        "PUT",
        "PATCH",
        "OPTIONS",
        "HEAD",
    },
)

# CORS
cors_config = CORSConfig(
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_methods=[
        "GET",
        "POST",
        "DELETE",
        "PUT",
        "PATCH",
        "OPTIONS",
        "HEAD",
    ],
    allow_headers=["Origin", "Content-Type", "X-CSRFToken", "Authorization"],
    allow_credentials=True,
)
