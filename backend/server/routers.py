"""Application Modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

from accounts import AuthController
from server import DatabaseController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler


route_handlers: list[ControllerRouterHandler] = [
    DatabaseController,
    AuthController,
]
