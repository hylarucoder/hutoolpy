import base64
import hashlib
import hmac

from cyberwander.contrib.crypto import hmac_sha1, hmac_sha256, hmac_md5, sha1, sha256, md5


def test_sha1():
    assert sha1(b"123456") == "7c4a8d09ca3762af61e59520943dc26494f8941b"


def test_sha256():
    assert (
        sha256(b"123456")
        == "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    )


def test_md5():
    assert md5(b"123456") == "e10adc3949ba59abbe56e057f20f883e"


def test_hmac_sha1():
    assert hmac_sha1(b"key", b"source") == b"/XHaIKIfbqOzTn/Bgr47Ek0X2kM="


def test_hmac_sha256():
    assert (
        hmac_sha256(b"key", b"source")
        == b"+mNy7n78m/usy4rFd/wqSYOF7ALboAXwHr0zVmvhJ8Q="
    )


def test_hmac_md5():
    assert hmac_md5(b"key", b"source") == b"3txdFNN/eL153raF7GcnRQ=="
