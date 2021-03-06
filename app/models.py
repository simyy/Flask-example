#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Text

from . import db

class Person(db.Model):
    __tablename__ = 'person'

    id   = Column(Integer, primary_key=True)
    name = Column(String(32)) 
    age  = Column(Integer)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return '<Person %s>' % self.id
