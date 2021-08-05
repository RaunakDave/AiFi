FROM python:3.8.1-alpine3.11
RUN apk update && apk add bash && apk add curl
COPY . /app
WORKDIR /app
RUN apk --no-cache add --virtual=.build-dep build-base git \
    && apk --no-cache add zeromq-dev libffi-dev \
    && python3 -m pip install --no-cache-dir git+https://github.com/locustio/locust.git@1.0.3#egg=locustio  \
    && apk del .build-dep
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
