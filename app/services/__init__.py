from celery import Celery

celery_service = Celery("email-service", broker='redis://localhost:6379/0')