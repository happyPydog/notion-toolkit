"""Notion common schema."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl
from .rich_text import RichText


class FileField(BaseModel):
    """File field."""

    url: HttpUrl = Field(
        description="URL of the file.",
        examples=[
            "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7b8b0713-dbd4-4962-b38b-955b6c49a573/My_test_image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221024T205211Z&X-Amz-Expires=3600&X-Amz-Signature=208aa971577ff05e75e68354e8a9488697288ff3fb3879c2d599433a7625bf90&X-Amz-SignedHeaders=host&x-id=GetObject"
        ],
    )
    expiry_time: datetime = Field(
        description="Expiry time of the file URL.",
        examples=["2022-10-24T22:49:22.765Z"],
    )


class File(BaseModel):
    """File object."""

    type: str = "file"
    file: FileField = Field(description="File object.")


class Emoji(BaseModel):
    """Emoji object."""

    type: str = "emoji"
    emoji: str = Field(description="The emoji character.", examples=["😻"])


class Date(BaseModel):
    """
    Date mention object.
    """

    start: str = Field(
        ...,
        description="start date",
        examples=["2022-01-01"],
    )
    end: str = Field(
        default=None,
        description="end date",
        examples=["2022-01-02", None],
    )


class Color(str, Enum):
    """
    Color of the text.
    """

    BLUE = "blue"
    BLUE_BACKGROUND = "blue_background"
    BROWN = "brown"
    BROWN_BACKGROUND = "brown_background"
    DEFAULT = "default"
    GRAY = "gray"
    GRAY_BACKGROUND = "gray_background"
    GREEN = "green"
    GREEN_BACKGROUND = "green_background"
    ORANGE = "orange"
    ORANGE_BACKGROUND = "orange_background"
    PINK = "pink"
    PINK_BACKGROUND = "pink_background"
    PURPLE = "purple"
    PURPLE_BACKGROUND = "purple_background"
    RED = "red"
    RED_BACKGROUND = "red_background"
    YELLOW = "yellow"
    YELLOW_BACKGROUND = "yellow_background"


class Title(BaseModel):
    """Title object."""

    id: str = "title"
    type: str = "title"
    title: RichText


class Checkbox(BaseModel):
    """Checkbox object."""

    checkbox: bool

class 