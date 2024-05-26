FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY ./entrypoint.sh /

EXPOSE 8000

ENTRYPOINT ["sh", "/entrypoint.sh"]
