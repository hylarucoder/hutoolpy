from collections import OrderedDict


def get_obj_attr(obj, field):
    """
    :param obj:
    :param field:
    :return:
    """
    for key in field.split("."):
        obj = getattr(obj, key)
        if obj is None:
            break
    return obj


def get_obj_key_fmt(keys):
    """
    :param keys:
    :return:
    'asset.asset_category.name' -> 'asset_asset_category_name' -> 'asset_category_name'
    """
    return "_".join(list(OrderedDict.fromkeys("_".join(keys.split(".")).split("_"))))


def unpack_obj(obj, *args, recurse=False):
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        fields = args[0]
    else:
        fields = args
    if not recurse:
        return {field: getattr(obj, field) for field in fields}
    else:
        return {get_obj_key_fmt(field): get_obj_attr(obj, field) for field in fields}
