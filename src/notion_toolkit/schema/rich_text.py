"""Common schema."""

from enum import Enum
from pydantic import BaseModel, Field, HttpUrl, UUID4


class NotionObjectType(str, Enum):
    """
    Notion object type.
    """

    BLOCK = "block"
    PAGE = "page"
    DATABASE = "database"
    USER = "user"
    COMMENT = "comment"
    DATABASE_PAGE = "database_page"


class RichTextObjectType(str, Enum):
    """
    Rich text object type.
    """

    TEXT = "text"
    EQUATION = "equation"
    MENTION = "mention"


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


class Annotations(BaseModel):
    """
    The information used to style the rich text object.Refer to the annotation object section below for details.
    """

    bold: bool = Field(
        default=False,
        description="Whether the text is bolded.",
        examples=[True, False],
    )
    italic: bool = Field(
        default=False,
        description="Whether the text is italicized.",
        examples=[True, False],
    )
    strikethrough: bool = Field(
        default=False,
        description="Whether the text is struck through.",
        examples=[True, False],
    )
    underline: bool = Field(
        default=False,
        description="Whether the text is underlined.",
        examples=[True, False],
    )
    code: bool = Field(
        default=False,
        description="Whether the text is code style",
        examples=[True, False],
    )
    color: Color = Field(
        default=Color.DEFAULT,
        description=f"Color of the text. Possible values include: {[c.value for c in Color]}",
        examples=[Color.BLUE, Color.DEFAULT, "default"],
    )


class MentionType(str, Enum):
    """
    The type of this mention.
    """

    DATABASE = "database"
    DATE = "date"
    LINK_PREVIEW = "link_preview"
    PAGE = "page"
    TEMPLATE_MENTION = "template_mention"
    USER = "user"


class Link(BaseModel):
    """
    An object with information about any inline link in this text, if included.
    """

    url: HttpUrl = Field(
        ...,
        description="web address",
        examples=["https://developers.notion.com/"],
    )


class ID(BaseModel):
    """
    Database mentions contain a database reference within the corresponding database field. A database reference is an object with an id key and a string value (UUIDv4) corresponding to a database ID.
    """

    id: UUID4


class DatabaseMentionObject(BaseModel):
    """
    Database mention object.
    """

    type: RichTextObjectType = Field(default=MentionType.DATABASE)
    database: ID = Field(
        ...,
        description="The database object.",
        examples=[{"id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"}],
    )


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


class DateMentionObject(BaseModel):
    """
    Date mention object.
    """

    type: RichTextObjectType = Field(default=MentionType.DATE)
    date: Date = Field(
        ...,
        description="The date object.",
        examples=[{"start": "2022-01-01", "end": "2022-01-02"}],
    )


class LinkPreviewMentionObject(BaseModel):
    """
    Link preview mention object.
    """

    type: RichTextObjectType = Field(default=MentionType.LINK_PREVIEW)
    link_preview: Link = Field(
        ...,
        description="The link preview object.",
        examples=[{"url": "https://developers.notion.com/"}],
    )


class PageMentionObject(BaseModel):
    """
    Page mention object.
    """

    type: RichTextObjectType = Field(default=MentionType.PAGE)
    page: ID = Field(
        ...,
        description="The page object.",
        examples=[{"id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"}],
    )


class TempalteMentionType(str, Enum):
    TEMPLATE_MENTION_DATE = "template_mention_date"
    TEMPLATE_MENTION_USER = "template_mention_user"


class TempalteMentionDateType(str, Enum):
    """
    The type of the date mention.
    """

    TODAY = "today"
    NOW = "now"


class TempalteMentionUserType(str, Enum):
    """
    The type of the user mention.
    """

    ME = "me"


class TemplateMentionFieldObject(BaseModel):
    """
    Template mention rich text objects contain a template_mention object with a nested type key that is either "template_mention_date" or "template_mention_user".
    """

    type: TempalteMentionType = Field(default=TempalteMentionType.TEMPLATE_MENTION_DATE)
    template_mention_date: TempalteMentionDateType = Field(
        default=None,
        description="The type of the date mention.",
        examples=[TempalteMentionDateType.TODAY, TempalteMentionDateType.NOW],
    )
    template_mention_user: TempalteMentionUserType = Field(
        default=None,
        description="The type of the user mention.",
        examples=[TempalteMentionUserType.ME],
    )


class TemplateMentionObject(BaseModel):
    """
    Template mention object.
    """

    type: RichTextObjectType = Field(default=MentionType.TEMPLATE_MENTION)
    template_mention: TemplateMentionFieldObject = Field(
        ...,
        description="The template field object.",
        examples=[{"type": "template_mention_date", "template_mention_date": "today"}],
    )


class User(BaseModel):
    """
    User mention object.
    """

    object: str = "user"
    id: UUID4


class UserMentionObject(BaseModel):
    """
    User mention object.
    """

    type: RichTextObjectType = Field(default=MentionType.USER)
    user: User = Field(
        ...,
        description="The user object.",
        examples=[{"id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"}],
    )


class MentionObject(BaseModel):
    """
    Rich text mention object.
    Mention objects represent an inline mention of a database, date, link preview mention, page, template mention, or user. A mention is created in the Notion UI when a user types @ followed by the name of the reference.
    """

    type: RichTextObjectType = Field(default=RichTextObjectType.MENTION)
    mention: (
        DatabaseMentionObject
        | DateMentionObject
        | LinkPreviewMentionObject
        | PageMentionObject
        | TemplateMentionObject
        | UserMentionObject
    ) = Field(
        ...,
        description="An object containing type-specific configuration. Refer to the mention type object sections below for details.",
        examples=[
            {
                "type": "database",
                "database": {"id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"},
            }
        ],
    )


class EquationObject(BaseModel):
    """
    Rich text equation object.
    Notion supports inline LaTeX equations as rich text object’s with a type value of "equation".
    """

    type: RichTextObjectType = Field(default=RichTextObjectType.EQUATION)
    expression: str = Field(
        ...,
        description="The LaTeX string representing the inline equation.",
        examples=["\frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}}", "E = mc^2"],
    )


class TextObject(BaseModel):
    """
    Rich text text object.
    """

    content: str = Field(
        ...,
        description="	The actual text content of the text.",
        examples=["Some words "],
    )
    link: Link | None = Field(
        default=None,
        description="An object with information about any inline link in this text, if included. If the text contains an inline link, then the object key is url and the value is the URL’s string web address. If the text doesn’t have any inline links, then the value is null.",
        examples=[{"url": "https://developers.notion.com/"}],
    )


class RichText(BaseModel):
    """
    Rich Text.

    Schema from official Notion API
        - https://developers.notion.com/reference/rich-text

    Limits:
        - text.content: 2000 characters
        - text.link.url: 2000 characters
        - equation.expression: 1000 characters
        - Any array of all block types, including rich text objects: 100 elements
    """

    type: RichTextObjectType
    text: TextObject | None = None
    mention: MentionObject | None = None
    equation: EquationObject | None = None
    annotations: Annotations = Field(
        ...,
        default_factory=Annotations,
        description="The information used to style the rich text object. Refer to the annotation object section below for details.",
        examples=[
            {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            }
        ],
    )
    plain_text: str = Field(
        default=...,
        description="The plain text without annotations.",
        examples=["Some words "],
    )
    href: str | None = Field(
        default=None,
        description="The URL of any link or Notion mention in this text, if any.",
        examples=["https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"],
    )

    @classmethod
    def create_for_text(cls, content: str, link: str | None = None) -> "RichText":
        return cls(
            type=RichTextObjectType.TEXT,
            text=(
                TextObject(content=content)
                if link is None
                else TextObject(content=content, link=Link(url=link))
            ),
            plain_text=content,
        )

    @classmethod
    def create_for_mention(cls):
        raise NotImplementedError

    @classmethod
    def create_for_equation(cls, expression: str) -> "RichText":
        return cls(
            type=RichTextObjectType.EQUATION,
            equation=EquationObject(expression=expression),
        )
