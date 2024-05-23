"""Database module."""

from typing import TYPE_CHECKING

from litestar import Controller, asgi
from piccolo.apps.user.tables import BaseUser
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin
from piccolo_api.session_auth.tables import SessionsBase

if TYPE_CHECKING:
    from litestar.types import Receive, Scope, Send


class DatabaseError(Exception):
    """Exception class for Database."""

    DATABASE_CONNECTION_ERROR = "Database connection error"
    DATABASE_CONNECTION_POOL_ERROR = "Database connection pool error"

    def __init__(self: any, message: str) -> None:
        """Initialize the exception."""
        super().__init__(message)


class DatabaseController(Controller):
    """DatabaseController."""

    path = "/"

    # mounting Piccolo Admin
    @asgi("/admin/", is_mount=True)
    async def admin(self: "DatabaseController", scope: "Scope", receive: "Receive", send: "Send") -> None:
        """Piccolo Admin."""
        await create_admin(
            tables=[BaseUser, SessionsBase]
        )(
            scope,
            receive,
            send,
        )


async def open_database_connection_pool() -> None:
    """Open a database connection pool."""
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception as e:
        raise DatabaseError(DatabaseError.DATABASE_CONNECTION_POOL_ERROR) from e


async def close_database_connection_pool() -> None:
    """Close a database connection pool."""
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception as e:
        raise DatabaseError(DatabaseError.DATABASE_CONNECTION_POOL_ERROR) from e
