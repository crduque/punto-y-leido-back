import os
import click
import flask_migrate
from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
import models
from seed_data import data

@click.command()
@with_appcontext
def init_db():
    load_seed_data(data)

def load_seed_data(data):
    for table, rows in data.items():
        if table == "written_by":
            print("hola")
            ModelClass = models[table]
        else:
            ModelClass = getattr(models, table)

        for row in rows:
            new_row = ModelClass(**row)
            models.db.session.merge(new_row)
            models.db.session.commit()
