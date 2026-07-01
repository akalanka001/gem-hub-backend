FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install uv and the system dependencies required to build psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

COPY . ./

RUN DJANGO_SECRET_KEY=dummy_build_key uv run python manage.py collectstatic --noinput

EXPOSE 5000

CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:5000", "--workers", "3"]