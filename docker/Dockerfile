FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/lib/python3.8/site-packages

ADD parser.py /usr/local/bin/parser.py
RUN set -ex \
  && chmod +x /usr/local/bin/parser.py \
  && apk add --no-cache py3-requests
EXPOSE 8080
ENTRYPOINT ["python","/usr/local/bin/parser.py"]
