import base64
import hashlib

from pydantic import BaseModel, validator, root_validator
from urllib.parse import urlparse


class UrlCreate(BaseModel):
    url: str
    short_url: str = None

    @validator('url')
    def name_must_contain_space(cls, value):
        parsed_url = urlparse(value)
        if not parsed_url.scheme and not parsed_url.netloc:
            raise ValueError('Invalid URL')
        return value

    @root_validator(pre=True)
    def root_validator(cls, values):
        url = values['url']
        hash_value = hashlib.sha256(url.encode()).digest()
        short_url = base64.urlsafe_b64encode(hash_value).decode()[:8]
        values['short_url'] = short_url
        return values
