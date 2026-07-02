#!/bin/bash
# Path: /opt/gem-hub-backend/.deploy/deploy.sh
set -e

echo "🚀 Starting Deployment..."

# 1. Build the web image specifically
docker compose build web

# 2. Start/Restart the container in the background without affecting other services
docker compose up -d --no-deps web

# 3. Apply database migrations
docker compose exec -T web uv run python manage.py migrate --noinput

# 4. Collect static files (optional, but good practice for Django)
docker compose exec -T web uv run python manage.py collectstatic --noinput

# 5. Cleanup unused images
docker image prune -f

echo "✅ Deployment Successful!"