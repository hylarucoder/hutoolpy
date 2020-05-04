import base64
import hashlib
import hmac


def hmac_sha1(secret: [bytes, str], source: [bytes, str]):
    if isinstance(source, str):
        source = bytes(source, "utf-8")
    if isinstance(secret, str):
        secret = bytes(secret, "utf-8")
    h = hmac.new(secret, source, hashlib.sha1)
    signature = str(base64.encodebytes(h.digest()).strip(), "utf-8")
    return signature


def hmac_md5(secret: [bytes, str], source: [bytes, str]):
    if isinstance(source, str):
        source = bytes(source, "utf-8")
    if isinstance(secret, str):
        secret = bytes(secret, "utf-8")
    h = hmac.new(secret, source, hashlib.md5)
    signature = str(base64.encodebytes(h.digest()).strip(), "utf-8")
    return signature


def rc4_encrypt(key, msg):
    pass


def rc4_decrypt(key, msg):
    pass
