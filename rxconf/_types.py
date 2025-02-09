import contextlib
import datetime as dt
import sys
import typing as tp


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

YAML_ATTRIBUTE_TYPE: TypeAlias = tp.Union[
    tp.Union[bool, int, str, float, None],
    tp.List[tp.Union[bool, int, str, float, None]],
    tp.Set[tp.Union[bool, int, str, float, None]],
    tp.Union[dt.date, dt.datetime],
]

JSON_ATTRIBUTE_TYPE: TypeAlias = tp.Union[
    tp.Union[bool, int, str, float, None],
    tp.List[tp.Union[bool, int, str, float, None]],
]

TOML_ATTRIBUTE_TYPE: TypeAlias = tp.Union[
    tp.Union[bool, int, str, float],
    tp.List[tp.Union[bool, int, str, float]],
    tp.Union[dt.date, dt.datetime],
]

INI_ATTRIBUTE_TYPE: TypeAlias = tp.Union[
    bool,
    int,
    str,
    float,
    None,
]

ENV_ATTRIBUTE_TYPE: TypeAlias = tp.Union[
    bool,
    int,
    str,
    float,
    None,
]

VAULT_ATTRIBUTE_TYPE: TypeAlias = tp.Union[
    tp.Union[bool, int, str, float, None],
    tp.List[tp.Union[bool, int, str, float, None]],
    tp.Set[tp.Union[bool, int, str, float, None]],
    tp.Union[dt.date, dt.datetime],
]


def map_primitive(value: str) -> tp.Union[int, float, bool, None, str]:
    """Unify the value from the whole configuration sources to a primitive type."""

    lower_value = value.lower()
    if lower_value in {"none", "null"}:
        return None
    if lower_value == "true":
        return True
    if lower_value == "false":
        return False
    with contextlib.suppress(ValueError):
        return int(value)
    with contextlib.suppress(ValueError):
        return float(value)
    return value
