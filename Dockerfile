FROM python:slim-buster

WORKDIR /schema_validator

COPY ./requirements.txt .

ENV PIP_ENV_VERSION=21.1.1
RUN python -m pip install --no-cache-dir --upgrade pip==${PIP_ENV_VERSION}

RUN python -m pip install --no-cache-dir -r ./requirements.txt

COPY . .

CMD ["main.py"]

ENTRYPOINT ["python3"]

