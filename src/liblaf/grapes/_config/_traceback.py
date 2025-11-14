from liblaf.grapes.conf import BaseConfig, Field, field


class ConfigTraceback(BaseConfig):
    indent_guide: Field[bool] = field(default=True)
    locals_hide_dunder: Field[bool] = field(default=True)
    locals_hide_sunder: Field[bool] = field(default=True)
    locals_max_length: Field[int] = field(default=10)
    locals_max_string: Field[int] = field(default=80)
    show_locals: Field[bool] = field(default=True)
    theme: Field[str] = field(default="ansi_dark")
