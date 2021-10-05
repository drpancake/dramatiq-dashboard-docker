#!/usr/bin/env python
import os

import bjoern
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq_dashboard import DashboardApp

REDIS_URL = os.environ['REDIS_URL']
REDIS_QUEUES = os.environ.get('REDIS_QUEUES', 'default')
REDIS_NAMESPACE = os.environ.get('REDIS_NAMESPACE', 'default')
PORT = int(os.environ.get('PORT', 8080))
HOST = os.environ.get('HOST', '0.0.0.0')

broker = RedisBroker(url=REDIS_URL, namespace=REDIS_NAMESPACE)
for queue in REDIS_QUEUES.split(','):
    broker.declare_queue(queue)
dramatiq.set_broker(broker)

app = DashboardApp(broker=broker, prefix='')
print(f'Starting @ http://{HOST}:{PORT}')
bjoern.run(app, HOST, PORT)
