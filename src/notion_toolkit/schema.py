"""Notion Schema."""

from enum import Enum
from typing import TypedDict


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


class AnotationObject(TypedDict):
    ...


class RichText(TypedDict):
    type: RichTextType
