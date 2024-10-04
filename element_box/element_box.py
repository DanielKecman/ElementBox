"""
Element Box
"""
from typing import Any, Callable, cast
from kecsoft_core.element_box.data_element import DataElement
from kecsoft_core.element_box.data_element_factory import create_data_element
from kecsoft_core.element_box.data_element_type import DataElementType
from kecsoft_core.element_box.data_element_optionality import DataElementOptionality
from kecsoft_core.utils.kecsoft_exception import create_kecsoft_exception, ErrorType


class ElementBox:
    def __init__(self,
                 name: str,
                 validation_function: Callable[[Any], None] = None):
        self._name: str = name
        self._elements: dict[str, DataElement] = {}
        self._validation_function: Callable[[ElementBox], None] = validation_function

    def __getitem__(self, item: str) -> DataElement:
        if item.split(" : ")[0] == item:
            return self.get_element(item)
        else:
            embedded_box, element_to_get = item.split(" : ", maxsplit=1)
            de = self.get_element(embedded_box)
            v: ElementBox = cast(ElementBox, de.value)
            return v[element_to_get]

    def to_string(self, outer_box_name: str = "") -> str:
        output_str = ""

        if outer_box_name == "":
            prefix = self._name
        else:
            prefix = outer_box_name

        for element_key in self._elements.keys():
            if self._elements[element_key].element_type == DataElementType.ELEMENT_BOX:
                prefix = f"{prefix} : {element_key}"
                output_str += self._elements[element_key].value.to_string(prefix)
            else:
                output_str += (f"{prefix} : {element_key} "
                           f"= {self._elements[element_key].value}\n")

        return output_str

    def add_element(self,
                    name: str,
                    element_type: DataElementType,
                    optionality: DataElementOptionality,
                    validation_function: Callable[[Any], None]) -> None:
        self._elements[name] = create_data_element(name,
                                                   element_type,
                                                   optionality,
                                                   self._name,
                                                   validation_function)

    def get_element(self, element_name: str) -> DataElement:
        if element_name not in self._elements.keys():
            raise create_kecsoft_exception(f"Referencing element <{element_name}> that doesn't exist in this box <{self._name}>",
                                           ErrorType.DATA_ISSUE,
                                           element_name,
                                           f"Element name in box <{self._name}>",
                                           "Referencing data element in box")
        return self._elements.get(element_name)

    def validate(self) -> None:
        for element in self._elements.values():
            element.validate()

        if self._validation_function is not None:
            self._validation_function(self)
