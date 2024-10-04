"""
Data Element INT list
"""
import datetime

import datefinder
from datetime import date
from typing import Callable, Any
from kecsoft_core.element_box.data_element import DataElement
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality
from kecsoft_core.utils.kecsoft_exception import create_kecsoft_exception, ErrorType


class DataElementListDate(DataElement):
    def __init__(self,
                 name: str,
                 optionality: DataElementOptionality,
                 box_name: str,
                 validation_function: Callable[[Any], None] = None):
        super().__init__(name, DataElementType.LIST_DATE, optionality, box_name, validation_function)

    def set_value_from_string(self, value: str):
        all_dates = list(datefinder.find_dates(value))
        number_dates = len(all_dates)

        if number_dates < 1:
            raise create_kecsoft_exception(f"No dates found in <{value}>",
                                           ErrorType.DATA_ISSUE,
                                           self.get_element_and_box_name(),
                                           "DataElementListDate",
                                           "Setting value from string")

        self.value = [each_date.date() for each_date in all_dates]
        self._is_loaded = True

    def _is_proper_type(self, value: Any) -> bool:
        if isinstance(value, list):
            for v in value:
                if not isinstance(v, date):
                    return False
            return True
        return False
