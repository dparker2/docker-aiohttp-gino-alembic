# docker-aiohttp-gino-alembic
Starter template repo for dockerized aiohttp application, using gino and alembic

# Setup
1. Build
```bash
docker-compose build
```
2. Generate initial migration
```bash
docker-compose run web alembic revision -m "Initialize schema" --autogenerate
```
3. Initialize database
```bash
docker-compose run web alembic upgrade head
```
4. Run app
```bash
docker-compose run web
```

# Play with the endpoints
```bash
$ curl localhost:8000/todo
{"todo": []}
```

```bash
$ curl -d '{"title":"Do the dishes"}' localhost:8000/tasks
{"task": {"id": 1, "title": "Do the dishes", "description": null, "is_completed": false}}
```

```bash
$ curl localhost:8000/todo
{"todo": [{"id": 1, "title": "Do the dishes", "description": null, "is_completed": false}]}
```

```bash
$ curl -X POST localhost:8000/tasks/1/complete
{"task": {"id": 1, "title": "Do the dishes", "description": null, "is_completed": true}}
```

```bash
$ curl localhost:8000/todo
{"todo": []}
```

# Add more
Try to extend this starting point. Here are some ideas for what to incorporate:
1. Authentication - OAuth, Token, JWT, etc
2. Authorization - Different permission levels for different endpoints
3. Response Serializers - Incorporate something like marshmallow to serialize complex objects
4. Request Validation - Use a schema validation library like marshmallow to validate incoming requests
5. General Error Handling - Catch errors in a middleware and format them consistently
6. Production Environment - Set up a Kubernetes cluster and create the specifications to run the app there
