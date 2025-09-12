import pydantic

from ._base import BaseConfig
from ._joblib import ConfigJoblib
from ._pretty import ConfigPretty


class Config(BaseConfig):
    joblib: ConfigJoblib = pydantic.Field(default_factory=ConfigJoblib)
    pretty: ConfigPretty = pydantic.Field(default_factory=ConfigPretty)


config = Config()
