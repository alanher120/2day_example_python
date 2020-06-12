FROM python:3.6

COPY src/app.py /app.py
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt
