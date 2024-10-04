"""
Data Element Box
"""

from typing import Callable, Any

import kecsoft_core.element_box.element_box
from kecsoft_core.element_box.data_element import DataElement
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality
from kecsoft_core.utils.kecsoft_exception import create_kecsoft_exception, ErrorType


class DataElementBox(DataElement):
    def __init__(self,
                 name: str,
                 optionality: DataElementOptionality,
                 box_name: str,
                 validation_function: Callable[[Any], None] = None):
        super().__init__(name, DataElementType.ELEMENT_BOX, optionality, box_name, validation_function)

    def set_value_from_string(self, value: str):
        raise create_kecsoft_exception(f"set_value_from_string not implemented for DataElementBox",
                                       ErrorType.PROCESSING_ISSUE,
                                       self.get_element_and_box_name(),
                                       f"Value setter in {self.get_element_and_box_name()}",
                                       "Setting value for element in data element box")

    def _is_proper_type(self, value: Any) -> bool:
        if not isinstance(value, kecsoft_core.element_box.element_box.ElementBox):
            return False
        return True
