"""
Data Element Factory
"""

from typing import Any, Callable

from kecsoft_core.element_box.data_element_box import DataElementBox
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality
from kecsoft_core.element_box.data_element_int import DataElementInt
from kecsoft_core.element_box.data_element_string import DataElementString
from kecsoft_core.element_box.data_element_float import DataElementFloat
from kecsoft_core.element_box.data_element_date import DataElementDate
from kecsoft_core.element_box.data_element_list_int import DataElementListInt
from kecsoft_core.element_box.data_element_list_string import DataElementListString
from kecsoft_core.element_box.data_element_list_float import DataElementListFloat
from kecsoft_core.element_box.data_element_list_date import DataElementListDate


def create_data_element(name: str,
                        element_type: DataElementType,
                        optionality: DataElementOptionality,
                        box_name: str,
                        validation_function: Callable[[Any], None] = None):

    if element_type == DataElementType.INT:
        return DataElementInt(name, optionality, box_name, validation_function)
    if element_type == DataElementType.STRING:
        return DataElementString(name, optionality, box_name, validation_function)
    if element_type == DataElementType.FLOAT:
        return DataElementFloat(name, optionality, box_name, validation_function)
    if element_type == DataElementType.DATE:
        return DataElementDate(name, optionality, box_name, validation_function)
    if element_type == DataElementType.ELEMENT_BOX:
        return DataElementBox(name, optionality, box_name, validation_function)
    if element_type == DataElementType.LIST_INT:
        return DataElementListInt(name, optionality, box_name, validation_function)
    if element_type == DataElementType.LIST_STRING:
        return DataElementListString(name, optionality, box_name, validation_function)
    if element_type == DataElementType.LIST_FLOAT:
        return DataElementListFloat(name, optionality, box_name, validation_function)
    if element_type == DataElementType.LIST_DATE:
        return DataElementListDate(name, optionality, box_name, validation_function)

    raise Exception(f"Unsupported type <{element_type}> in data element factory")
