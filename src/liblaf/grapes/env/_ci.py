from environs import env


def ci() -> bool:
    return env.bool("CI", False) or env.bool("GITHUB_ACTIONS", False)
