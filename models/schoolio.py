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
    data = UnicodeAttribute(null=True)
    date = UTCDateTimeAttribute(null=True)
    first_name = UnicodeAttribute(null=True)
    grade = NumberAttribute(null=True)
    last_name = UnicodeAttribute(null=True)
    name = UnicodeAttribute(null=True)
    title = UnicodeAttribute(null=True)

    # Indexes
    data_index = DataIndex()
