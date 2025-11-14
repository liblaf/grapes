import attrs
from rich.syntax import Syntax, SyntaxTheme


@attrs.define
class RichTracebackOptions:
    indent_guide: bool = True
    locals_hide_dunder: bool = True
    locals_hide_sunder: bool = True
    locals_max_length: int = 10
    locals_max_string: int = 80
    theme: SyntaxTheme = attrs.field(factory=lambda: Syntax.get_theme("ansi_dark"))
