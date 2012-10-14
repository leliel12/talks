#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

example_db = SqliteDatabase('example.db')

class ExampleModel(Model):
    class Meta:
        database = example_db


class User(ExampleModel):
    name = CharField()


class Car(ExampleModel):
    model = CharField(null=True)
    plate = CharField(unique=True)
    user = ForeignKeyField(User, related_name="cars")

# Creamos las tablas si no existen
User.create_table(fail_silently=True)
Car.create_table(fail_silently=True)


