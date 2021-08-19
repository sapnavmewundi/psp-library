import os
from celery import Celery

def get_celery():
    ''' Returns a redis backed celery instance '''

    if os.environ['REDIS_URL']:
        redis = os.environ['REDIS_URL']
        celery = Celery(
            'util.tasks', backend=redis, broker=redis, include=[
                'worker.tasks'], config_source='worker.celeryconfig')
        return celery
    else:
        raise EnvironmentError("Please set REDIS_URL env variable")