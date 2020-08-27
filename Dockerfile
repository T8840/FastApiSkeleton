FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="T8840"

COPY ./app /app

RUN pip install -r /app/requirements.txt -i https://pypi.douban.com/simple