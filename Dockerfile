FROM alpine:3.22.1

WORKDIR /app/

COPY app.py requirements.txt /app/

RUN apk update && \
    apk add --no-cache \
        python3 \
        glib \
        pango \
        font-dejavu && \
    python3 -m venv .venv && \
    ./.venv/bin/pip3 install --upgrade pip && \
    ./.venv/bin/pip3 install -r requirements.txt

CMD [".venv/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:8082", "app:app"]
