import os

from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
)

from models.data_index import DataIndex


class Schoolio(Model):
    class Meta:
        table_name = os.environ.get('SCHOOLIO_TABLE_NAME', 'schoolio-funsies')

    # Table Attributes
    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    data = UnicodeAttribute()
    date = UTCDateTimeAttribute()
    first_name = UnicodeAttribute()
    grade = NumberAttribute()
    last_name = UnicodeAttribute()
    name = UnicodeAttribute()
    title = UnicodeAttribute()

    # Indexes
    data_index = DataIndex()
