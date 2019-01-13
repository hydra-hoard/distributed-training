FROM python:3.6

WORKDIR /
COPY . .

RUN sh build.sh

CMD ["sh","run.sh"]