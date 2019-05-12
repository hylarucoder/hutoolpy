def is_blank(s: [str, None]):
    """
    判断是否为空(除去空格换行)
    :param s:
    :return:
    """
    return s is None or len(s.strip()) == 0


def is_empty(s: [str, None]):
    """
    判断是否为空(包含空格字符)
    :param s:
    :return:
    """
    return s is None or len(s) == 0


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
HALF2FULL[0x20] = 0x3000

FULL2HALF = dict((i + 0xFEE0, i) for i in range(0x21, 0x7F))
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
