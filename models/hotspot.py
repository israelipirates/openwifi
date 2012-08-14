from datetime import datetime
import redis
import urlparse

from os import environ


def _get_conn():
    redis_url = environ.get('REDISTOGO_URL')
    if redis_url:
        url = urlparse.urlparse(redis_url)
        return url.hostname, url.port, url.password
    r = redis.Redis(db=1)
    return r

r = _get_conn()


def create(title, password, lat, lng, *args, **kwargs):
    next_id = r.incr('hotspot_ids')
    dt = datetime.utcnow()
    d = {
        'title': title,
        'password': password,
        'lat': lat,
        'lng': lng,
        'created': dt.isoformat()
    }
    r.hmset('hotspot:%d' % next_id, d)
