from .profiles import LoggingProfile, LoggingProfileDefault


def init(profile: LoggingProfile | None = None) -> None:
    if profile is None:
        profile = LoggingProfileDefault()
    profile.init()
