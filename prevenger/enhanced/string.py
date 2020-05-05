from typing import Union
import re


def is_blank(s: Union[str, None]):
    """
    判断是否为空(除去空格换行)
    "字符串为 null 或者内部字符全部为 ' ' '\t' '\n' '\r' 这四类字符时返回 true"
    """
    return s is None or len(s.strip()) == 0


def not_blank(s: Union[str, None]):
    raise is_blank(s)


def is_empty(s: Union[str, None]):
    """
    判断是否为空(包含空格字符)
    """
    return s is None or len(s) == 0


def not_empty(s: Union[str, None]):
    """
    判断是否为空(包含空格字符)
    """
    return is_empty(s)


def snake_to_camel_case(s):
    components = s.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_to_snake_case(s):
    """
    Taken from
    https://gist.github.com/zhy0216/a1a8c1d1ee3eebba86b91288b22ec7e2
    """
    groups = []
    sub_group = [s[0].lower()]
    for c in s[1:]:
        if 97 <= ord(c) <= 122:
            sub_group.append(c)
        else:
            groups.append("".join(sub_group))
            sub_group = [c.lower()]

    groups.append("".join(sub_group))
    return "_".join(groups)


def capitalize(s: str) -> str:
    return s.capitalize()


def approximate_equal(actual, expected, min_length=5, accepted_rate=0.8):
    """
    利用字符串近似算法进行近似比较
    :param actual:
    :param expected:
    :param min_length:
    :param accepted_rate:
    :return:
    """
    raise NotImplementedError()


HALF2FULL = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
FULL2HALF = dict((i + 0xFEE0, i) for i in range(0x21, 0x7F))
HALF2FULL[0x20] = 0x3000

FULL2HALF[0x3000] = 0x20


def full_to_half_width(_str):
    """
    Convert all ASCII characters to the full-width counterpart.
    """
    return str(_str).translate(FULL2HALF)


def half_to_full_width(_str):
    """
    Convert full-width characters to ASCII counterpart
    """
    return str(_str).translate(HALF2FULL)


def LevenshteinDistance(s, t):
    """字符串相似度算法（Levenshtein Distance算法）
  一个字符串可以通过增加一个字符，删除一个字符，替换一个字符得到另外一个
  字符串，假设，我们把从字符串A转换成字符串B，前面3种操作所执行的最少
  次数称为AB相似度
  这算法是由俄国科学家Levenshtein提出的。
  Step Description
  1 Set n to be the length of s.
    Set m to be the length of t.
    If n = 0, return m and exit.
    If m = 0, return n and exit.
    Construct a matrix containing 0..m rows and 0..n columns.
  2 Initialize the first row to 0..n.
    Initialize the first column to 0..m.
  3 Examine each character of s (i from 1 to n).
  4 Examine each character of t (j from 1 to m).
  5 If s[i] equals t[j], the cost is 0.
    If s[i] doesn't equal t[j], the cost is 1.
  6 Set cell d[i,j] of the matrix equal to the minimum of:
    a. The cell immediately above plus 1: d[i-1,j] + 1.
    b. The cell immediately to the left plus 1: d[i,j-1] + 1.
    c. The cell diagonally above and to the left plus the cost:
       d[i-1,j-1] + cost.
  7 After the iteration steps (3, 4, 5, 6) are complete, the distance is
    found in cell d[n,m]. """

    m, n = len(s), len(t)
    if not (m and n):
        return m or n

    # 构造矩阵
    matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
    matrix[0] = list(range(n + 1))
    for i in range(m + 1):
        matrix[i][0] = i

    for i in range(m):
        for j in range(n):
            cost = int(s[i] != t[j])
            # 因为 Python 的字符索引从 0 开始
            matrix[i + 1][j + 1] = min(
                matrix[i][j + 1] + 1,  # a.
                matrix[i + 1][j] + 1,  # b.
                matrix[i][j] + cost,  # c.
            )

    return matrix[m][n]


valid_similarity = LevenshteinDistance

"""
@Author: twocucao
@Email: twocucao@gmail.com
@Date: 2016-09-19
@Desc: 常用正则表达式,用于抽取/验证/替换
是整数? 是小数? 是QQ? 是日期? 是链接? 是IP? 银行卡? 电子邮箱? 其他
参考实现:
https://github.com/madisonmay/CommonRegex/blob/master/commonregex.py
http://blog.jobbole.com/96052/
"""

PT_CHINESE = r"([\u4e00-\u9fa5]+)+?"
PT_CHINESE_AND_NUMBER = r"([\u4e00-\u9fa5\d\w]+)+?"
PT_CLEAN_WORDS = r"([\u4e00-\u9fa5\d\s\a\w]+)+?"
PT_CHINESE_ID_CARD = r"([0-9]){7,18}(x|X)?"
PT_CHINESE_MOB_NUM = (
    r"(?:13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}"
)
PT_CHINESE_TELEPHONE = r"\d{3}-\d{8}|\d{4}-\d{7}"
PT_CHINESE_MONEY = r"¥\s*\d+"
PT_CHINESE_PRICE = r"[$]\s?[+-]?[0-9]{1,3}(?:(?:,?[0-9]{3}))*(?:\.[0-9]{1,2})?"
PT_CHINESE_SENTENCE = r"[\u4e00-\u9fa5]{1,}"
PT_TIME = r""
PT_DATE = r""
PT_DATETIME = r""
PT_DOMAIN = r"[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?"
PT_EMAIL = r"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"  # noqa
PT_HEX_COLOR = r"(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\\b"
PT_HTTP_HTTPS_LINK = r""
PT_INT_NUM = r"[0-9]*"
PT_IP_V4 = r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"  # noqa
PT_IP_V6 = r"\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*"  # noqa
PT_PREFERRED_DATE = r"\d{4}-\d{1,2}-\d{1,2}"
PT_PREFERRED_DATE_TIME = r""
PT_QQ_NUM = r"[1-9][0-9]{4,}"
PT_UUID = r"[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}"


def filter_chinese_characters(_str):
    new_str = re.sub(PT_CHINESE_SENTENCE, "", _str)
    return new_str


def filter_chinese_punctuations(_str):
    new_str = re.sub(r"[\s+.!/_,$%^*(\"']+|[+—！，。？、~@#￥%…&*（）：；《》“”()»〔〕-]+", "", _str)
    return new_str


def filter_all_chinese_things(_str):
    new_str = filter_chinese_punctuations(filter_chinese_characters(_str))
    return new_str


def filter_numbers(_str):
    new_str = re.sub(r"\d+", "", _str)
    return new_str


def filter_english_characters(_str):
    raise NotImplementedError()


ch_puncs = ["！", "，", "。", "？", "、", "（", "）", "：", "；", "《", "》", "“ ", "” "]
en_puncs = ["!", ",", ".", "?", ",", "(", ")", ":", ";", "<", ">", '"', '"']


def sub_chinese_punctuations(_str):
    """
    :param _str:
    :return:
    """
    for k, v in zip(ch_puncs, en_puncs):
        _str = _str.replace(k, v)
    return _str


def shrink_repeated4bilibili(_str, word_len=20):
    """
    :param _str:
    :param max_times:
    :param word_len:
    :return:
    """

    _str = re.sub(r"\s+", " ", _str)
    for i in range(1, word_len + 1):
        if i <= 3:
            max_times = 3
        elif i <= 5:
            max_times = 2
        else:
            max_times = 1
        _str = shrink_repeated_with_len(_str, max_times=max_times, word_len=i)
    return _str


def shrink_repeated(_str, max_times=3, word_len=20):
    """
    :param _str:
    :param max_times:
    :param word_len:
    :return:
    """

    _str = re.sub(r"\s+", " ", _str)
    for i in range(1, word_len + 1):
        _str = shrink_repeated_with_len(_str, max_times=max_times, word_len=i)
    return _str


def shrink_repeated_with_len(_str, max_times=3, word_len=3):
    """
    :param _str:
    :param max_times:
    :param word_len:
    n 为支持的字符串长度
    n 为 3 ,max_times 为3的时候 周杰伦周杰伦周杰伦周杰伦周杰伦 -> 周杰伦周杰伦周杰伦
    :return:
    """
    pat = r"(" + r"." * word_len + r")\1{%d,}" % max_times
    repl = r"".join([r"\1" for i in range(max_times)])
    return re.sub(pat, repl, _str)


def shrink_online_rent(_str):
    _str = sub_chinese_punctuations(_str)
    _str = shrink_repeated(_str, 4)
    return _str


"""
这是对HTML文本处理的一些常见的方案,主要是通过BeautifulSoup实现,主要用户处理常见的一些HTML处理和提取.
"""


def html_escape_chars_to_string(_str):
    return (
        _str
        if is_empty(_str)
        else _str.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&amp;", "&")
        .replace("&quot;", '"')
    )


def extract_links_from_html(_str):
    raise NotImplementedError()


def shrink_string(_str, strip_chars=None, nullable=True):
    """
    :param _str:
    :param nullable:
    :param strip_chars:
    :return:
    """
    if isinstance(_str, str):
        if strip_chars is None:
            return _str.strip()
        else:
            return _str.strip(strip_chars)
    if nullable:
        return None
    else:
        return ""


def re_strip_or_none(_str, strips=" ", replaces=""):
    if isinstance(_str, str):
        _str = _str.strip(strips + " ").replace(replaces, "")
        if len(_str) == 0:
            return None
        return _str
    else:
        return None


chinese_digits_mapping = {
    "零": 0,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10000,
    "０": 0,
    "１": 1,
    "２": 2,
    "３": 3,
    "４": 4,
    "５": 5,
    "６": 6,
    "７": 7,
    "８": 8,
    "９": 9,
    "壹": 1,
    "贰": 2,
    "叁": 3,
    "肆": 4,
    "伍": 5,
    "陆": 6,
    "柒": 7,
    "捌": 8,
    "玖": 9,
    "拾": 10,
    "佰": 100,
    "仟": 1000,
    "萬": 10000,
    "亿": 100000000,
}


def digits_to_chinese(digit: str):
    """
    :param digit:
    :return:
    author: binux(17175297.hk@gmail.com)
    modified by: twocucao
    """
    count = 0
    result = 0
    tmp = 0
    billion = 0
    while count < len(digit):
        tmp_chr = digit[count]
        tmp_num = chinese_digits_mapping.get(tmp_chr)
        # 如果等于1亿
        if tmp_num == 100000000:
            result += tmp
            result = result * tmp_num
            # 获得亿以上的数量，将其保存在中间变量Billion中并清空result
            billion = billion * 100000000 + result
            result = 0
            tmp = 0
        # 如果等于1万
        elif tmp_num == 10000:
            result += tmp
            result = result * tmp_num
            tmp = 0
        # 如果等于十或者百，千
        elif tmp_num >= 10:
            if tmp == 0:
                tmp = 1
            result += tmp_num * tmp
            tmp = 0
        # 如果是个位数
        elif tmp_num is not None:
            tmp = tmp * 10 + tmp_num
        count += 1
    result = result + tmp
    result = result + billion
    return result
