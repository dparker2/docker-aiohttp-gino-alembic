from aiohttp import web
from app.db import tasks


async def index(request):
    return web.Response(text="Hello, world!")


async def todo_list(request):
    todo = await tasks.select().where(tasks.c.is_completed == False).gino.all()
    return web.json_response(dict(todo=[dict(t.items()) for t in todo]))


async def create_task(request):
    body = await request.json()
    if "title" not in body:
        return web.HTTPBadRequest()

    task = (
        await tasks.insert()
        .returning(tasks)
        .values(title=body.get("title"), description=body.get("description"))
        .gino.first()
    )

    return web.json_response(dict(task=dict(task.items())))


async def get_task(request):
    try:
        task_id = int(request.match_info["task"])
    except ValueError:
        return web.HTTPBadRequest()

    task = await tasks.select().where(tasks.c.id == task_id).gino.first()
    if task is None:
        return web.HTTPNotFound()

    return web.json_response(dict(task=dict(task.items())))


async def complete_task(request):
    try:
        task_id = int(request.match_info["task"])
    except ValueError:
        return web.HTTPBadRequest()

    task = (
        await tasks.update()
        .returning(tasks)
        .where(tasks.c.id == task_id)
        .values(is_completed=True)
        .gino.first()
    )
    if task is None:
        return web.HTTPNotFound()

    return web.json_response(dict(task=dict(task.items())))
