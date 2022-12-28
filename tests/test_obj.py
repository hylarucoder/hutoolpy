import dataclasses

from hutoolpy.obj import unpack_obj


@dataclasses.dataclass
class Inner:
    d: str


@dataclasses.dataclass
class Outer:
    a: int
    b: int
    inner: Inner


def test_unpack_obj():
    d = Outer(a=1, b=2, inner=Inner(d=3))
    dd = unpack_obj(d, "a", "b", "inner.d", recurse=True)
    assert dd == {"a": 1, "b": 2, "inner_d": 3}
