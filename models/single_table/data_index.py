from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UnicodeAttribute


class DataIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        # index_name is optional, but can be provided to override the default name
        index_name = 'data_index'
        # All attributes are projected
        projection = AllProjection()
        read_capacity_units = 2
        write_capacity_units = 2

    # This attribute is the hash key for the index
    # Note that this attribute must also exist
    # in the model
    sk = UnicodeAttribute(hash_key=True)
    data = UnicodeAttribute(range_key=True)
