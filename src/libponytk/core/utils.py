import re


RE_SLUG = re.compile(ur'[a-z0-9A-Z](?:[a-z0-9A-Z-_.])+')

def is_valid_slug(s):
    mo = RE_SLUG.match(s)
    return mo is not None
