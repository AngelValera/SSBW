FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r ./django_app/requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "django_app", "mi_sitio_web.wsgi:application"]
#CMD ["python", "django_app/manage.py", "runserver", "0.0.0.0:8000"]