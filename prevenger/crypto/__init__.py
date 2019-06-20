import base64
import hashlib


def md5(s, encoding="utf-8"):
    m = hashlib.md5()
    m.update(s.encode(encoding))
    return m.hexdigest()
