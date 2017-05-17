FROM python:3.6

WORKDIR /app
ADD ./requirements.txt /app
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
COPY . /app

CMD ["sh", "run.sh"]

