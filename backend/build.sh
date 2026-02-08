#!/usr/bin/env bash
# Build script for Render

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input --clear
python manage.py migrate

# Auto-create admin superuser
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Admin user created')
EOF