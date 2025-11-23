from rich.tree import Tree

from liblaf.grapes.logging.helpers import LoggerTree


def test_logger_tree() -> None:
    tree = LoggerTree()
    assert "root" in tree
    assert isinstance(tree["root"], Tree)
