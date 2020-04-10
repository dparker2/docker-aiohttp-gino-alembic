from aiohttp import web
from app import views


def setup_routes(app):
    app.add_routes(
        [
            web.get("/", views.index),
            web.post("/tasks", views.create_task),
            web.get("/tasks/{task}", views.get_task),
            web.post("/tasks/{task}/complete", views.complete_task),
            web.get("/todo", views.todo_list),
        ]
    )
