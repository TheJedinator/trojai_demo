FROM python:3.9-buster

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app
RUN chmod +x /app/run.sh

CMD /app/run.sh