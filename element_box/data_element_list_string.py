"""
Data Element STRING list
"""

from typing import Callable, Any
from kecsoft_core.element_box.data_element import DataElement
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality


class DataElementListString(DataElement):
    def __init__(self,
                 name: str,
                 optionality: DataElementOptionality,
                 box_name: str,
                 validation_function: Callable[[Any], None] = None):
        super().__init__(name, DataElementType.LIST_STRING, optionality, box_name, validation_function)

    def set_value_from_string(self, value: str):
        self.value = value.split(",")
        self._is_loaded = True

    def _is_proper_type(self, value: Any) -> bool:
        if isinstance(value, list):
            for v in value:
                if not isinstance(v, str):
                    return False
            return True
        return False
