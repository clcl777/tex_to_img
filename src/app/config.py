from flask import Flask
import os


def set_config(app: Flask):
    app.config.update(
        SECRET_KEY='dev',
        WTF_CSRF_SECRET_KEY='csrf',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://{user}:{password}@{host}:5432/{name}'.format(**{
            'user': os.environ['POSTGRES_USER'],
            'password': os.environ['POSTGRES_PASSWORD'],
            'host': os.environ['HOST'],
            'name': os.environ['NAME']
        })
    )
