# Flask

### Get started
```sh
    export FLASK_APP=main.py
    export FLASK_ENV=development
    flask run --host=0.0.0.0
```

### Migrate
Usage:

    pip install Flask-Migrate
    flask db init
    flask db migrate
    flask db upgrade
    sort_keys=False