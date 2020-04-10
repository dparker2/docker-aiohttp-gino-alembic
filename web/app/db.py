from os import environ
from gino.ext.aiohttp import Gino


db = Gino()

tasks = db.Table(
    "tasks",
    db,
    db.Column("id", db.BigInteger(), primary_key=True),
    db.Column("title", db.Unicode(), nullable=False),
    db.Column("description", db.Unicode()),
    db.Column("is_completed", db.Boolean(), default=False),
)


def setup_db(app):
    app.middlewares.append(db)
    db.init_app(
        app,
        config=dict(
            host=environ["DB_HOST"],
            port=environ["DB_PORT"],
            user=environ["DB_USER"],
            password=environ["DB_PASS"],
            database=environ["DB_NAME"],
        ),
    )
