"""Guards for the accounts app."""

from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

from litestar.exceptions import NotAuthorizedException
from piccolo.apps.user.tables import BaseUser
from piccolo_api.session_auth.tables import SessionsBase

if TYPE_CHECKING:
    from litestar import Request
    from litestar.connection import ASGIConnection
    from litestar.handlers.base import BaseRouteHandler


class CustomNotAuthorizedException(NotAuthorizedException):
    """Custom exception for NotAuthorizedException."""

    Message = "You are not authorized to access this resource."
    USER_NOT_FOUND = "User not found."


# guard for protected endpoints
def current_user_guard(
    connection: ASGIConnection,
    _: BaseRouteHandler,
) -> None:
    """Guard for protected endpoints."""
    if not connection.cookies.get("id"):
        raise NotAuthorizedException()


async def current_user(request: Request) -> dict[str, t.Any]:
    """Get current user."""
    data = (
        await SessionsBase.select(SessionsBase.user_id)
        .where(SessionsBase.token == request.cookies.get("id"))
        .first()
        .run()
    )
    if data:
        session_user = (
            await BaseUser.select(
                BaseUser.id,
                BaseUser.username,
                BaseUser.email,
                BaseUser.last_login,
            )
            .where(BaseUser.id == data["user_id"])
            .first()
            .run()
        )
    return {"user": session_user}
