"""
Data Element DATE
"""

import datefinder
from datetime import date
from typing import Any, Callable
from kecsoft_core.element_box.data_element import DataElement
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality
from kecsoft_core.utils.kecsoft_exception import create_kecsoft_exception, ErrorType


class DataElementDate(DataElement):
    def __init__(self,
                 name: str,
                 optionality: DataElementOptionality,
                 box_name: str,
                 validation_function: Callable[[Any], None] = None):
        super().__init__(name, DataElementType.DATE, optionality, box_name, validation_function)

    def set_value_from_string(self, value: str):
        found_dates = list(datefinder.find_dates(value))
        how_many: int = len(found_dates)

        if how_many != 1:
            raise create_kecsoft_exception(f"Couldn't convert string <{value}> to date",
                                           ErrorType.DATA_ISSUE,
                                           self.get_element_and_box_name(),
                                           "DataElementDate",
                                           "Calling set_value_from_string")

        self._value = found_dates[0].date()
        self._is_loaded = True

    def _is_proper_type(self, value: Any) -> bool:
        return isinstance(value, date)
