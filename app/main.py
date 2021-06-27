from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes.api import router as api_router
from core.config import ALLOWED_HOSTS, API_PREFIX


def get_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=API_PREFIX)
    return app


app = get_app()
