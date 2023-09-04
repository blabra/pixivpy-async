from dataclasses import dataclass

from dacite import from_dict


def to_dataclass(target_class: dataclass, src_dict: dict):
    return from_dict(target_class, src_dict)
