from hutoolpy.json import (
    json_snake_to_camel_case,
    json_camel_to_snake_case,
    json_equal,
)

camel_json = {
    "firstKey": "first value",
    "secondKey": "second value",
    "thirdKey": [
        {"subThirdKey": 1},
        {"subThirdKey2": 2},
        {"subThirdKey3": [{"superDeep": "wow"}]},
    ],
}

snake_json = {
    "first_key": "first value",
    "second_key": "second value",
    "third_key": [
        {"sub_third_key": 1},
        {"sub_third_key2": 2},
        {"sub_third_key3": [{"super_deep": "wow"}]},
    ],
}


def test_json_snake_and_camel():
    assert json_equal(json_camel_to_snake_case(camel_json), snake_json)
    assert json_equal(json_snake_to_camel_case(snake_json), camel_json)
