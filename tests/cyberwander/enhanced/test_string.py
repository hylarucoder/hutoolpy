from cyberwander.enhanced.string import camel_to_snake_case, snake_to_camel_case


def test_camel_to_snake_case():
    assert "a" == camel_to_snake_case("A")
    assert "a_b_c" == camel_to_snake_case("ABC")
    assert "abc" == camel_to_snake_case("ABC", False)
    assert "ab_c" == camel_to_snake_case("AbC")
    assert "a_bc" == camel_to_snake_case("ABc")
    assert "ab_cd" == camel_to_snake_case("AbCd")
    assert "sub_third_key2" == camel_to_snake_case("subThirdKey2")


def test_snake_to_camel_case():
    assert snake_to_camel_case("a") == "a"
    assert snake_to_camel_case("a_b_c") == "aBC"
    assert snake_to_camel_case("ab_c") == "abC"
    assert snake_to_camel_case("a_bc") == "aBc"
    assert snake_to_camel_case("ab_cd") == "abCd"
    assert snake_to_camel_case("sub_third_key2") == "subThirdKey2"
