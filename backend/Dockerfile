FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "--capture-output", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

