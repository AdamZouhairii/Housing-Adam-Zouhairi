FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

CMD ["python", "consumer.py"]