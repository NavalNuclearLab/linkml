# Auto generated from pattern_1.yaml by pythongen.py version: 0.0.1
# Generation date: 2000-01-01T00:00:00
# Schema: pattern_1
#
# id: http://example.org/test/pattern_1
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PATTERN = CurieNamespace('pattern', 'http://example.org/test/pattern_1/')
DEFAULT_ = PATTERN


# Types

# Class references
class DiskDeviceLabel(extended_str):
    pass


@dataclass(repr=False)
class DiskDevice(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN["DiskDevice"]
    class_class_curie: ClassVar[str] = "pattern:DiskDevice"
    class_name: ClassVar[str] = "DiskDevice"
    class_model_uri: ClassVar[URIRef] = PATTERN.DiskDevice

    label: Union[str, DiskDeviceLabel] = None
    device: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, DiskDeviceLabel):
            self.label = DiskDeviceLabel(self.label)

        if self.device is not None and not isinstance(self.device, str):
            self.device = str(self.device)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.device = Slot(uri=PATTERN.device, name="device", curie=PATTERN.curie('device'),
                   model_uri=PATTERN.device, domain=None, range=Optional[str],
                   pattern=re.compile(r'^/dev/[^/]+(/[^/]+)*$'))

slots.label = Slot(uri=PATTERN.label, name="label", curie=PATTERN.curie('label'),
                   model_uri=PATTERN.label, domain=None, range=URIRef,
                   pattern=re.compile(r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'))
