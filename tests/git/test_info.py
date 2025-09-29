from liblaf import grapes


def test_url_parse() -> None:
    parsed: grapes.git.GitInfo = grapes.git.info()
    assert parsed.platform == "github"
    assert parsed.owner == "liblaf"
    assert parsed.repo == "grapes"
