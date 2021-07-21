try:
    # python2
    from urllib import urlencode
except ImportError:
    # python3
    from urllib.parse import urlencode


def to_queryparams(obj: dict) -> str:
    obj_striped = {
        k.strip(): v.strip() if isinstance(v, str) else v
        for k, v in obj.items()
    }
    return urlencode(obj_striped)
