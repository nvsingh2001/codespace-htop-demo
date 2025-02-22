FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    procps \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo "Asia/Kolkata" > /etc/timezone

WORKDIR /app
COPY server.py /app

RUN pip install flask pytz

EXPOSE 3000

CMD ["python", "server.py"]
