python manage.py makemigrations
python manage.py migrate

exec "daphne" "-b" "0.0.0.0" "-p" "8000" "flow.asgi:application"
