"""
adapted from: https://github.com/said-ali/iterable_orm
"""
from __future__ import annotations

from functools import reduce
from itertools import filterfalse
from operator import attrgetter
from typing import TypeVar


class ObjectDoesNotExist(Exception):
    pass


class MultipleObjectsReturned(Exception):
    pass


def lookups(filter):
    return {
        "gt": lambda obj_value, value: obj_value > value,
        "gte": lambda obj_value, value: obj_value >= value,
        "lt": lambda obj_value, value: obj_value < value,
        "lte": lambda obj_value, value: obj_value <= value,
        "startswith": lambda obj_value, value: obj_value.startswith(value),
        "istartswith": lambda obj_value, value: obj_value.lower().startswith(value.lower()),
        "endswith": lambda obj_value, value: obj_value.endswith(value),
        "contains": lambda obj_value, value: value in obj_value,
        "icontains": lambda obj_value, value: value.lower() in obj_value.lower(),
        "not_equal_to": lambda obj_value, value: obj_value != value,
        "in": lambda obj_value, value: obj_value in value,
        "not_in": lambda obj_value, value: obj_value not in value,
        "range": lambda obj_value, range_values: range_values[0] <= obj_value <= range_values[1],
        "date_range": lambda obj_value, range_values: range_values[0].isoformat()
        <= obj_value.isoformat()
        <= range_values[1].isoformat(),
    }.get(filter, None)


RepoItem = TypeVar("RepoItem")


class MemoryRepo:
    def __init__(self, queryset: list[RepoItem]):
        # TODO: support for lazy?
        self._data = list(queryset)

    @property
    def _queryset(self):
        return self._data

    def __iter__(self):
        return iter(self._queryset)

    def __getitem__(self, index) -> RepoItem:
        return self._queryset[index]

    def __len__(self) -> int:
        return len(self._queryset)

    def _copy(self, queryset) -> MemoryRepo:
        return self.__class__(queryset)

    def order_by(self, key) -> MemoryRepo:
        reverse = False
        if "-" in key:
            reverse = True
            key = key.replace("-", "")
        return self._copy(
            sorted(
                self._queryset,
                key=attrgetter(key.replace("__", ".")),
                reverse=reverse,
            )
        )

    def _filter_or_exclude(self, **kwargs) -> MemoryRepo:
        """Used for filter and exclude returns a function to be used by itertool."""

        def _filter(obj):
            for key, value in kwargs.items():
                field_lookup = lookups(key.split("__")[-1])
                lookup_key = key.replace("__", ".").split(".")

                # It looks like a function has been passed
                if hasattr(value, "__call__"):
                    if not value(reduce(getattr, lookup_key, obj)):
                        return False
                    continue

                if field_lookup:
                    # Since there's field_lookup, remove the last element which is a look up value such as gt,
                    # startswith etc.
                    lookup_key.pop()
                    lookup_match = field_lookup(reduce(getattr, lookup_key, obj), value)
                    if not lookup_match:
                        return False
                    continue

                field_match = reduce(getattr, lookup_key, obj) == value
                if not field_match:
                    return False
            return True

        return _filter

    def filter(self, **kwargs) -> MemoryRepo:
        return self._copy(filter(self._filter_or_exclude(**kwargs), self._queryset))

    def exclude(self, **kwargs) -> MemoryRepo:
        return self._copy(filterfalse(self._filter_or_exclude(**kwargs), self._queryset))

    def exists(self) -> bool:
        return bool(self)

    def count(self) -> bool:
        return len(self)

    def all(self) -> list[RepoItem]:
        return self._copy(self._queryset)

    def as_dict(self, *keys) -> dict[tuple, RepoItem]:
        d = {}
        for item in self._copy(self._queryset):
            d[tuple(getattr(item, key) for key in keys)] = item
        return d

    def first(self) -> RepoItem:
        if self._queryset:
            return self._queryset[0]
        return None

    def last(self) -> RepoItem:
        if self._queryset:
            return self._queryset[-1]
        return None

    def find_first(self, **kwargs):
        clone = self.filter(**kwargs)
        if clone:
            return clone[0]
        return None

    def get(self, **kwargs) -> RepoItem:
        clone = self.filter(**kwargs)
        num = len(clone)
        if num == 1:
            return clone[0]
        if not num:
            raise ObjectDoesNotExist("Matching query does not exist.")

        if len(clone) > 1:
            raise MultipleObjectsReturned("get() returned more than one -- it returned {num}!".format(num=num))
