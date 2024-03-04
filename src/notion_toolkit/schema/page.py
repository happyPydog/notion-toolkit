from enum import Enum
from uuid import uuid4, UUID
from datetime import datetime
from pydantic import BaseModel, Field, UUID4, HttpUrl
from .rich_text import NotionObjectType
from .common import File, Emoji
from .parent import DatabaseParent, PageParent, WorkspaceParent, BlockParent


class PagePropertyType(str, Enum):
    """
    The type of the property in the page object.
    """

    CHECKBOX = "checkbox"


class PageProperties(BaseModel):
    """
    Property values of this page. As of version 2022-06-28, properties only contains the ID of the property; in prior versions properties contained the values as well.

    - If parent.type is "page_id" or "workspace", then the only valid key is title.
    - If parent.type is "database_id", then the keys and values of this field are determined by the properties of the database this page belongs to.

    key string Name of a property as it appears in Notion.
    value object See [Property value object](https://developers.notion.com/reference/property-value-object).
    """

    id: str
    type: str


class ProdCopilotSourceDatabasePageProperties(BaseModel):
    Name: Title
    Archived: Checkbox


class BasePageRequestBody(BaseModel):
    """
    The Page object contains the page property values of a single Notion page.
    """

    object: str = Field(
        ...,
        description="Always page.",
        examples=["page", NotionObjectType.PAGE],
    )
    id: UUID4 = Field(
        ...,
        description="Unique identifier of the page.",
        examples=[uuid4(), UUID("a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b")],
    )
    created_time: datetime = Field(
        default=None,
        description="Date and time when this page was created. Formatted as an ISO 8601 date time string.",
        examples=["2020-03-17T19:10:04.968Z"],
    )
    created_by: datetime = Field(
        default=None,
        description="User who created the page.",
        examples=[{"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}],
    )
    last_edited_time: datetime = Field(
        default=None,
        description="Date and time when this page was updated. Formatted as an ISO 8601 date time string.",
        examples=["2020-03-17T19:10:04.968Z"],
    )
    last_edited_by: str = Field(
        default=None,
        description="User who last edited the page.",
        examples=[{"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}],
    )
    archived: str = Field(
        default=False,
        description="The archived status of the page.",
        examples=[True, False],
    )
    icon: File | Emoji = Field(
        default=None,
        description="Page icon.",
    )
    cover: File = Field(
        default=None,
        description="Page cover image.",
    )
    properties: PageProperties = Field(
        default_factory=PageProperties,
        description="Page property values.",
    )
    parent: DatabaseParent | PageParent | WorkspaceParent | BlockParent = Field(
        default=None,
        description="Information about the page's parent.",
    )
    url: HttpUrl = Field(
        default=None,
        description="The URL of the Notion page.",
        examples=["https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"],
    )
    public_url: HttpUrl = Field(
        default=None,
        description="The public page URL if the page has been published to the web. Otherwise, null.",
        examples=["https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"],
    )


class ProdCopilotSourceDatabasePageRequestBody(BasePageRequestBody):
    properties: PageProperties


class PageResponseBody(PageRequestBody):
    """
    The Page object contains the page property values of a single Notion page.
    """
