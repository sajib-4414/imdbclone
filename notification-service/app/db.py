# app/db.py
from tortoise.models import Model
from tortoise import fields

class User(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(pk=True)
    username:str = fields.CharField(max_length=255, unique=True)
    email:str = fields.CharField(max_length=255, unique=True)
    active: bool = fields.BooleanField(default=True, nullable=False)

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return self.name