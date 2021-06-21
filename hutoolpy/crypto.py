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


CAESAR_TABLE = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"


def caesar_encode(message: str, offset: int):
    length = len(CAESAR_TABLE)
    chars = []
    for _char in message:
        char = CAESAR_TABLE[(CAESAR_TABLE.index(_char) + offset) % length]
        chars.append(char)
    return "".join(chars)


def caesar_decode(message: str, offset: int):
    length = len(CAESAR_TABLE)
    chars = []
    for _char in message:
        char = CAESAR_TABLE[(CAESAR_TABLE.index(_char) + length - offset) % length]
        chars.append(char)
    return "".join(chars)


# TODO: morse 密码
