FROM python:3.10.2-slim-buster


COPY requirements.txt /root/requirements.txt
RUN pip install --upgrade pip && \
    pip install --ignore-installed -r /root/requirements.txt

WORKDIR /root/app

COPY . /root/app

EXPOSE 80

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]