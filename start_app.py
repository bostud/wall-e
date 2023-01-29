from fastapi import FastAPI

from api.routes import register_routes
from config import DEBUG

app = FastAPI(
    debug=DEBUG,
    title='Wall-E API',
    docs_url='/api/docs',
)
register_routes(app)
