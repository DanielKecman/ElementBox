"""
Data Element Type
"""

from enum import Enum


class DataElementType(Enum):
    INT = "int"
    STRING = "str"
    FLOAT = "float"
    DATE = "date"
    ELEMENT_BOX = "element_box"
    LIST_INT = "list[int]"
    LIST_STRING = "list[string]"
    LIST_FLOAT = "list[float]"
    LIST_DATE = "list[date]"
    # LIST_ELEMENT_BOX = "list[element_box]"
