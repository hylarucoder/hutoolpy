"""
# 无限迭代器
count(10, 2) -> 10, 10 + 2*1, 10 + 2*2, …
cycle("ABCD")
repeat(10, 3) --> 10 10 10
tee
"""

import itertools


def test_itertools():
    assert list(itertools.accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]

    assert list(itertools.chain(*["ABC", "DEF"])) == ["A", "B", "C", "D", "E", "F"]
    assert list(itertools.chain.from_iterable(["ABC", "DEF"])) == [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    # map
    assert list(map(lambda x: x[0] ** x[1], [(2, 5), (3, 2), (10, 3)])) == [32, 9, 1000]
    assert list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])) == [32, 9, 1000]
    # 过滤
    assert list(itertools.filterfalse(lambda x: x % 2, range(10))) == [0, 2, 4, 6, 8]
    assert list(filter(lambda x: x % 2, range(10))) == [1, 3, 5, 7, 9]
    assert list(itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 1])) == [
        "A",
        "C",
        "E",
        "F",
    ]
    assert list(itertools.islice([1, 4, 6, 4, 1, 6, 1, 3], 3)) == [1, 4, 6]
    # 取第一个false之前的值
    assert list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1, 6])) == [1, 4]
    # 取第一个false之后的值
    assert list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1, 6, 1, 3])) == [
        6,
        4,
        1,
        6,
        1,
        3,
    ]
    # groupby
    assert ["".join(g) for k, g in itertools.groupby("AAAAACCBDA")] == [
        "AAAAA",
        "CC",
        "B",
        "D",
        "A",
    ]

    # zip
    assert list(zip("ABCD", "223")) == [("A", "2"), ("B", "2"), ("C", "3")]
    assert list(itertools.zip_longest("ABCD", "223", fillvalue="1")) == [
        ("A", "2"),
        ("B", "2"),
        ("C", "3"),
        ("D", "1"),
    ]

    # 笛卡尔乘积 ABCD x ABCD
    assert list(itertools.product("ABCD", repeat=2)) == [
        ("A", "A"),
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("B", "A"),
        ("B", "B"),
        ("B", "C"),
        ("B", "D"),
        ("C", "A"),
        ("C", "B"),
        ("C", "C"),
        ("C", "D"),
        ("D", "A"),
        ("D", "B"),
        ("D", "C"),
        ("D", "D"),
    ]

    # 排列 ABCD
    assert list(itertools.permutations("ABCD", 2)) == [
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("B", "A"),
        ("B", "C"),
        ("B", "D"),
        ("C", "A"),
        ("C", "B"),
        ("C", "D"),
        ("D", "A"),
        ("D", "B"),
        ("D", "C"),
    ]
    # 组合 ABCD
    assert list(itertools.combinations("ABCD", 2)) == [
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("B", "C"),
        ("B", "D"),
        ("C", "D"),
    ]
    # 组合 ABCD 包含 AA
    assert list(itertools.combinations_with_replacement("ABCD", 2)) == [
        ("A", "A"),
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("B", "B"),
        ("B", "C"),
        ("B", "D"),
        ("C", "C"),
        ("C", "D"),
        ("D", "D"),
    ]
