import base64
import hashlib
import hmac


def sha1(message: bytes) -> str:
    return hashlib.sha1(message).hexdigest()


def sha256(message: bytes) -> str:
    return hashlib.sha256(message).hexdigest()


def md5(message: bytes) -> str:
    return hashlib.md5(message).hexdigest()


"""
# Hash-based Message Authentication Code
HMAC运算利用哈希算法，以一个密钥和一个消息为输入，生成一个消息摘要作为输出。
hmac-sha1 与 sha1不一样
"""


def hmac_sha1(secret: bytes, source: bytes) -> bytes:
    h = hmac.new(secret, source, hashlib.sha1)
    return base64.encodebytes(h.digest()).strip()


def hmac_sha256(secret: bytes, source: bytes) -> bytes:
    h = hmac.new(secret, source, hashlib.sha256)
    return base64.encodebytes(h.digest()).strip()


def hmac_md5(secret: bytes, source: bytes) -> bytes:
    h = hmac.new(secret, source, hashlib.md5)
    return base64.encodebytes(h.digest()).strip()


# TODO: caesar 密码
# TODO: morse 密码
