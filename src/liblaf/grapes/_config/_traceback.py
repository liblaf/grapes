from liblaf.grapes import conf
from liblaf.grapes.conf import BaseConfig, Field


class ConfigTraceback(BaseConfig):
    indent_guide: Field[bool] = conf.bool(default=True)
    locals_hide_dunder: Field[bool] = conf.bool(default=True)
    locals_hide_sunder: Field[bool] = conf.bool(default=True)
    locals_max_length: Field[int] = conf.int(default=10)
    locals_max_string: Field[int] = conf.int(default=80)
    show_locals: Field[bool] = conf.bool(default=True)
    theme: Field[str] = conf.str(default="ansi_dark")
