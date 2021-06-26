from typing import Callable

from fastapi import FastAPI


def start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        pass

    return start_app


def stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        pass

    return stop_app
