import hashlib


def md5(s, encoding="utf-8"):
    m = hashlib.md5()
    m.update(s.encode(encoding))
    return m.hexdigest()


def sha1(s, encoding="utf-8"):
    m = hashlib.md5()
    m.update(s.encode(encoding))
    return m.hexdigest()


def sha256(s, encoding="utf-8"):
    m = hashlib.md5()
    m.update(s.encode(encoding))
    return m.hexdigest()


"""
caesar 密码
"""

"""
morse 密码
"""
