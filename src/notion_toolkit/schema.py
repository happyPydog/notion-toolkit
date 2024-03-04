"""Notion Schema."""

from enum import Enum
from pydantic import BaseModel, Field


class ObjectType(str, Enum):
    """Object type."""

    BLOCK = "block"
    PAGE = "page"
    DATABASE = "database"
    USER = "user"
    COMMENT = "comment"
    DATABASE_PAGE = "database_page"


class RichTextType(str, Enum):
    """The type of this rich text object."""

    TEXT = "text"
    MENTION = "mention"
    EQUATION = "equation"


class Equation(BaseModel):
    expression: str


class MentionType(str, Enum):
    """The type of this mention."""

    DATABASE = "database"
    DATE = "date"
    LINK_PREVIEW = "link_preview"
    PAGE = "page"
    TEMPLATE_MENTION = "template_mention"
    USER = "user"


class Mention(BaseModel):
    type: MentionType


class RichText(BaseModel):
    type: RichTextType
    annotations: Annotations
    plain_text: str
    href: str | None = None
    text: dict | None = None
    mention: dict | None = None
    equation: dict | None = None


RichText(
    type=RichTextType.TEXT,
    annotations=Annotations(bold=True),
    plain_text="This is bold text",
)


def create_rich_text(type: RichTextType) -> RichText:
    """Create rich text object."""
    return RichText(
        type=type,
        annotations=Annotations(bold=True),
        plain_text="This is bold text",
    )
