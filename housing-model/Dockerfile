FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

EXPOSE 8001
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]