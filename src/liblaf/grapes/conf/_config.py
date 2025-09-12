import pydantic

from ._base import BaseConfig
from ._joblib import ConfigJoblib


class Config(BaseConfig):
    joblib: ConfigJoblib = pydantic.Field(default_factory=ConfigJoblib)


config = Config()
