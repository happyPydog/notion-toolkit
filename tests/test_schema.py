"""Testing notion shcema."""

from notion_toolkit.schema import Color, Annotations


def test_color():
    assert Color.DEFAULT == "default"


def test_annotations():
    default_annotations = Annotations(
        bold=False,
        italic=False,
        strikethrough=False,
        underline=False,
        code=False,
        color="default",
    )
    assert Annotations() == default_annotations
