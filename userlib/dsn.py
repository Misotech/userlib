from urllib.parse import urlparse
from typing import NamedTuple


class DBCredentials(NamedTuple):
    database: str
    user: str
    password: str
    host: str
    port: str


def parse_dsn(dsn):
    parts = urlparse(dsn)
    return DBCredentials(
        database=parts.path.strip('/'),
        user=parts.username,
        host=parts.hostname,
        port=parts.port,
        password=parts.password
    )

