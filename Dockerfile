FROM python:slim-buster
COPY . .

ENV PIP_ENV_VERSION=21.1.1
RUN python -m pip install --no-cache-dir --upgrade pip==${PIP_ENV_VERSION}

RUN python -m pip install --no-cache-dir -r ./requirements.txt

CMD ["main.py"]
ENTRYPOINT ["python3"]
