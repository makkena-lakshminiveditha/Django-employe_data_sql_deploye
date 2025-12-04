python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn employe_data.wsgi:application --bind 0.0.0.0:$PORT