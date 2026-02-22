import datetime

import wadler_lindig as wl


def pdoc_datetime(obj: datetime.date, **_kwargs) -> wl.AbstractDoc:
    return wl.TextDoc(obj.isoformat())
