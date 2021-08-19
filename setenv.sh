#!/bin/sh
source bioenv/bin/activate
export PATH="$PATH:/Users/ppatharde/PycharmProjects/bioproject"
export REDIS_URL="redis://127.0.0.1:6379"
export SQLALCHEMY_DATABASE_URI="mysql://root:root@127.0.0.1:8889/bioproject"
celery worker -A worker.tasks -l info -P gevent -n worker1@%h