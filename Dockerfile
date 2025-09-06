FROM alpine:3.22.1

WORKDIR /app/

COPY app.py requirements.txt /app/

RUN apk update && \
    apk add --no-cache \
        python3 && \
    python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt && \
    .venv/bin/

CMD [".venv/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:8082", "app:app"]
