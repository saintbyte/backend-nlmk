from __future__ import annotations

import datetime
from peewee import AutoField
from peewee import DecimalField
from peewee import DateTimeField



from .base import BaseModel


class AtmosphereParameters(BaseModel):
    id = AutoField(primary_key=True)
    date = DateTimeField(default=datetime.datetime.now)
    temperature = DecimalField(max_digits=10, decimal_places=3)
    pressure = DecimalField(max_digits=10, decimal_places=3)
    humidity = DecimalField(max_digits=10, decimal_places=3)


