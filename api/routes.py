from fastapi import FastAPI, APIRouter

# routes
from api.handlers.json import json_router
from api.handlers.proto import proto_router


def register_routes(app: FastAPI) -> FastAPI:
    # API ROUTER
    api_router = APIRouter(prefix='/api', tags=['api'])
    api_router.include_router(json_router)
    api_router.include_router(proto_router)

    # Build Routes
    app.include_router(api_router)

    return app
