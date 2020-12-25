import json
from typing import Iterable, Dict, List

from cyberwander.enhanced.string import snake_to_camel_case, camel_to_snake_case


def get_ordered_json(obj):
    if isinstance(obj, dict):
        return sorted((k, get_ordered_json(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(get_ordered_json(x) for x in obj)
    else:
        return obj


def json_equal(obj1, obj2):
    # return json.dumps(obj1, sort_keys=True) == json.dumps(obj2, sort_keys=True)
    return obj1 == obj2


def json_keys_equal(obj1, obj2):
    # TODO:
    return get_ordered_json(obj1) == get_ordered_json(obj2)


def map_list_keys(func, objs: List):
    new_objs = []
    for obj in objs:
        if isinstance(obj, dict):
            new_objs.append(map_dict_keys(func, obj))
        else:
            new_objs.append(obj)
    return new_objs


def map_dict_keys(func, obj: Dict):
    new_obj = {}
    for key, value in obj.items():
        func_key = func(key)
        if isinstance(value, dict):
            new_obj[func_key] = func(value)
        if isinstance(value, list):
            new_obj[func_key] = map_list_keys(func, value)
        else:
            new_obj[func_key] = value
    return new_obj


def json_snake_to_camel_case(obj: Dict) -> Dict:
    return map_dict_keys(snake_to_camel_case, obj)


def json_camel_to_snake_case(obj: Dict) -> Dict:
    return map_dict_keys(camel_to_snake_case, obj)
