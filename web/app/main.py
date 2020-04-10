from asyncio import get_event_loop
from aiohttp import web
from app.routes import setup_routes
from app.db import setup_db


def create_app(loop):
    app = web.Application(loop=loop)
    setup_routes(app)
    setup_db(app)
    return app


if __name__ == "__main__":
    web.run_app(create_app(get_event_loop()))
