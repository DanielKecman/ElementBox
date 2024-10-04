"""
Data Element
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Optional
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality
from kecsoft_core.utils.kecsoft_exception import create_kecsoft_exception, ErrorType


class DataElement(ABC):
    def __init__(self,
                 name: str,
                 element_type: DataElementType,
                 optionality: DataElementOptionality,
                 box_name: str,
                 validation_function: Callable[[Any], None] = None):
        self._name: str = name
        self._element_type: DataElementType = element_type
        self._optionality: DataElementOptionality = optionality
        self._box_name: str = box_name
        self._validation_function: Optional[Callable[[], None]] = validation_function
        self._value: Optional[Any] = None
        self._is_loaded: bool = False

    def __str__(self) -> str:
        if not self._is_loaded:
            return "<Not set>"
        return f"{self._value}"

    @property
    def element_type(self) -> DataElementType:
        return self._element_type

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        if self.is_loaded:
            raise create_kecsoft_exception(f"Data Element <{self.get_element_and_box_name()}> already set",
                                           ErrorType.DATA_ISSUE,
                                           self.get_element_and_box_name(),
                                           "Data Element",
                                           "Setting data element value")

        if not self._is_proper_type(value):
            raise create_kecsoft_exception(f"Given value <{value}> is type {type(value)}, "
                                           f"expected {self._element_type.value}",
                                           ErrorType.DATA_ISSUE,
                                           self.get_element_and_box_name(),
                                           "Value for data element",
                                           "Setting data element value")

        self._value = value
        self._is_loaded = True

    @property
    def is_loaded(self) -> bool:
        return self._is_loaded

    @property
    def is_mandatory(self) -> bool:
        return self._optionality == DataElementOptionality.MANDATORY

    @abstractmethod
    def set_value_from_string(self, value: str) -> None:
        pass

    def get_name(self) -> str:
        return self._name

    def get_element_and_box_name(self) -> str:
        if self._box_name == "":
            return self._name
        return f"{self._box_name} : {self._name}"

    @abstractmethod
    def _is_proper_type(self, value: Any) -> bool:
        pass

    def validate(self) -> None:
        if self.is_mandatory:
            if not self.is_loaded:
                raise create_kecsoft_exception(f"Mandatory data element "
                                               f"<{self.get_element_and_box_name()}> is not loaded",
                                               ErrorType.DATA_ISSUE,
                                               self.get_element_and_box_name(),
                                               "Data Element",
                                               "Data Element Validation")

        if (self._validation_function is not None
                and (self.is_mandatory or self.is_loaded)):
            self._validation_function(self)

        if self._element_type == DataElementType.ELEMENT_BOX and (self.is_mandatory or self.is_loaded):
            self.value.validate()
