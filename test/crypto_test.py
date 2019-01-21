import pytest
import ujson
from userlib.crypto import Crypter


def test_encode_decode():

    t = b'1989411066620381'

    p = {'hello': {'name': 'unknown'}}
    c = Crypter(t)

    enc = c.encode(p)
    result = c.decode(enc)

    assert ujson.dumps(p) == ujson.dumps(result)





