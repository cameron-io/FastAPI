FROM python:alpine
WORKDIR /var/lib/fast_api
ADD requirements.txt .
RUN apk update && \
    apk upgrade && \
    apk --no-cache add make && \
    pip install --no-cache-dir "fastapi[standard]"
RUN pip3 install -r requirements.txt
ADD . .
RUN source .env
CMD fastapi dev app/main.py --host='0.0.0.0' --port=8000
