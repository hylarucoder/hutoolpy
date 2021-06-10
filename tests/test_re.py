import pytest

from hutoolpy.string import (
    PT_CHINESE_ID_CARD,
    PT_CHINESE_MOB_NUM,
    PT_CHINESE_MONEY,
    PT_CHINESE_TELEPHONE,
)
from hutoolpy.re import has_pattern


@pytest.mark.parametrize(
    "test_pattern,test_input,expected",
    [
        (PT_CHINESE_ID_CARD, "321323199509234453", True),
        (PT_CHINESE_ID_CARD, "爱是321323199509234453爱上的离开", True),
        (PT_CHINESE_ID_CARD, "1321323199509234453", True),
        (PT_CHINESE_MOB_NUM, "15123232033", True),
        (PT_CHINESE_MOB_NUM, "115123232033", True),
        (PT_CHINESE_MONEY, "¥ 115123232033", True),
        (PT_CHINESE_MONEY, "¥115123232033", True),
        (PT_CHINESE_MONEY, "苏州臭豆腐¥ 115123 / 人", True),
        (PT_CHINESE_MONEY, "中华人民共和国", False),
        (PT_CHINESE_MONEY, "¥115123232033", True),
        (PT_CHINESE_TELEPHONE, "0528-22332222", True),
        (PT_CHINESE_TELEPHONE, "000528-332222", False),
    ],
)
def test_has_pattern(test_pattern, test_input, expected):
    assert has_pattern(test_input, test_pattern) == expected


@pytest.mark.parametrize(
    "test_pattern,test_input,expected",
    [
        (PT_CHINESE_ID_CARD, "321323199509234453", True),
        (PT_CHINESE_ID_CARD, "爱是321323199509234453爱上的离开", False),
        (PT_CHINESE_ID_CARD, "1321323199509234453", True),
        (PT_CHINESE_MOB_NUM, "15123232033", True),
        (PT_CHINESE_MOB_NUM, "115123232033", False),
        (PT_CHINESE_MONEY, "¥ 115123232033", True),
        (PT_CHINESE_MONEY, "¥115123232033", True),
        (PT_CHINESE_MONEY, "苏州臭豆腐¥ 115123 / 人", False),
        (PT_CHINESE_MONEY, "中华人民共和国", True),
        (PT_CHINESE_MONEY, "¥115123232033", False),
        (PT_CHINESE_TELEPHONE, "0528-22332222", True),
        (PT_CHINESE_TELEPHONE, "000528-332222", False),
    ],
)
def test_match_pattern(test_pattern, test_input, expected):
    # assert match_pattern(test_input, test_pattern) == expected
    pass
