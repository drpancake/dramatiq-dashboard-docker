dramatiq-dashboard-docker
=========================

Runs the official (very alpha) Dramatiq dashboard in a Docker container behind
a standalone bjoern webserver.

How to run it
-------------

```sh
docker run -e REDIS_URL="redis://some-host:6379" -p 8080:8080 drpancake/dramatiq-dashboard:latest
```

Configurable environment variables
----------------------------------

- REDIS_URL (you must supply this, e.g. `redis://some-host:6379`)
- REDIS_QUEUES (defaults to `default`, it can be a comma-separated list)
- REDIS_NAMESPACE (defaults to `default`)
- HOST (defaults to `0.0.0.0`)
- PORT (defaults to `8080`)
