FROM python:3.13-slim AS builder

ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1000
ENV PGID ${PGID}

RUN groupadd -g ${PGID} user && \
    useradd -l -u ${PUID} -g user -m user && \
    usermod -p "*" user -s /bin/bash

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

CMD ["sh", "entrypoint.sh"]