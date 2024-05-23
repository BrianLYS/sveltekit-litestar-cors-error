"""Define Pydantic models for user registration and login."""

import typing as t

from piccolo.apps.user.tables import BaseUser
from piccolo_api.crud.serializers import create_pydantic_model
from pydantic import Field

# user models
BaseUserModelRegister: t.Any = create_pydantic_model(
    table=BaseUser,
    include_columns=(
        BaseUser.username,
        BaseUser.email,
        BaseUser.password,
    ),
    model_name="UserModelRegister",
)
BaseUserModelLogin: t.Any = create_pydantic_model(
    table=BaseUser,
    include_columns=(
        BaseUser.username,
        BaseUser.password,
    ),
    model_name="UserModelLogin",
)


class UserModelRegister(BaseUserModelRegister):
    """User registration model."""

    username: str = Field(..., example="john_doe")
    email: str = Field(..., example="john_doe@example.com")
    password: str = Field(..., example="securePassword123")


class UserModelLogin(BaseUserModelLogin):
    """User login model."""

    username: str = Field(..., example="john_doe")
    password: str = Field(..., example="securePassword123")
