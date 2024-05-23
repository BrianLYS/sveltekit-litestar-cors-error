"""Define the endpoints for the accounts app."""

from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING, ClassVar

from accounts.guards import current_user, current_user_guard
from accounts.schema import UserModelLogin, UserModelRegister
from litestar.controller import Controller
from litestar.datastructures import Cookie
from litestar.exceptions import NotAuthorizedException
from litestar.handlers import delete, get, post
from litestar.response import Response
from litestar.status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from piccolo.apps.user.tables import BaseUser
from piccolo_api.session_auth.tables import SessionsBase

if TYPE_CHECKING:
    from accounts.schema import UserModelLogin, UserModelRegister
    from litestar import Request



class AuthController(Controller):
    """Authentication controller."""

    path = "/accounts"
    tags: ClassVar[list[str]] = ["Accounts"]

    @post("/register")
    async def register(self: AuthController, data: UserModelRegister) -> Response:
        """Register user."""
        payload = data.dict()
        if (
            await BaseUser.exists().where(BaseUser.email == payload["email"]).run()
            or await BaseUser.exists().where(BaseUser.username == payload["username"]).run()
        ):
            user_error = "User with that email or username already exists."
            return Response(
                content={"error": user_error},
                status_code=HTTP_400_BAD_REQUEST,
            )

        # save user
        query = BaseUser(**payload)
        await query.save().run()
        return Response(
            content={"message": "User created"},
            status_code=HTTP_201_CREATED,
        )

    @post("/login")
    async def login(self: AuthController, data: UserModelLogin) -> Response:
        """Login and authenticate user."""
        payload = data.dict()
        # login user in
        valid_user: t.Any = await BaseUser.login(
            username=payload["username"],
            password=payload["password"],
        )
        if not valid_user:
            response = Response(
                content={"message": "Invalid username or password"},
                status_code=HTTP_401_UNAUTHORIZED,
            )
        else:
            # create session
            session = await SessionsBase.create_session(user_id=valid_user)
            token = session["token"]  # retrieve the token from the session
            response = Response(
                content={"message": "Succesfully logged in", "token": token},
                status_code=HTTP_201_CREATED,
                cookies=[
                    Cookie(
                        key="id",
                        value=f"{session['token']}",
                        max_age=3600,
                        httponly=True,
                    ),
                ],
            )
        return response

    @get("/validate_token", guards=[current_user_guard])
    async def validate_token(self: AuthController, request: Request) -> Response:
        """Validate token."""
        try:
            user = await current_user(request)
            response = Response(
                content={"message": "Token is valid", "user": user},
                status_code=HTTP_200_OK,
            )
        except NotAuthorizedException:
            response = Response(
                content={"message": "Token is invalid or missing"},
                status_code=HTTP_401_UNAUTHORIZED,
            )
        return response

    @post("/logout")
    async def logout(self: AuthController) -> Response:
        """Logout user."""
        response = Response(
            content={"message": "Succesfully logged out"},
            status_code=HTTP_201_CREATED,
        )
        response.delete_cookie(key="id")
        return response

    @get("/profile", guards=[current_user_guard])
    async def profile(self: AuthController, request: Request) -> dict[str, t.Any]:
        """User profile."""
        return await current_user(request)

    @delete("/delete", guards=[current_user_guard])
    async def delete_user(self: AuthController, request: Request) -> None:
        """Delete user."""
        session_user = await current_user(request)
        await (
            BaseUser.delete()
            .where(
                BaseUser.id == session_user["user"]["id"],
            )
            .run()
        )

        response = Response(
            content=None,
            status_code=HTTP_204_NO_CONTENT,
        )
        response.delete_cookie(key="id")
