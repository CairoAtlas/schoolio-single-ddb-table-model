import os

from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
)


class Schoolio(Model):
    class Meta:
        table_name = os.environ['SCHOOLIO_TABLE_NAME']

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    data = UnicodeAttribute()
    date = UTCDateTimeAttribute()
    first_name = UnicodeAttribute()
    grade = NumberAttribute()
    last_name = UnicodeAttribute()
    name = UnicodeAttribute()
    title = UnicodeAttribute()
