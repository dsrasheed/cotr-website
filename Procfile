web: gunicorn -w 4 cotr:app
worker: celery worker -A cotr.celery -l debug
