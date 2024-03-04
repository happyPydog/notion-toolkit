"""Page Properties schema."""

from enum import Enum
from pydantic import BaseModel, EmailStr


class PagePropertyType(str, Enum):
    """
    The type of the property in the page object.
    """

    CHECKBOX = "checkbox"
    CREATED_BY = "created_by"
    CREATED_TIME = "created_time"
    DATE = "date"
    EMAIL = "email"
    FILES = "files"
    FORMULA = "formula"
    LAST_EDITED_BY = "last_edited_by"
    LAST_EDITED_TIME = "last_edited_time"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    PEOPLE = "people"
    PHONE_NUMBER = "phone_number"
    RELATION = "relation"
    ROLLUP = "rollup"
    RICH_TEXT = "rich_text"
    SELECT = "select"
    STATUS = "status"
    TITLE = "title"
    URL = "url"
    UNIQUE_ID = "unique_id"


class Checkbox(BaseModel): ...


class CreatedBy(BaseModel): ...


class CreatedTime(BaseModel): ...


class Date(BaseModel): ...


class Email(BaseModel):
    email: EmailStr


class Formula(BaseModel): ...


class LastEditedBy(BaseModel): ...


class LastEditedTime(BaseModel): ...


class MultiSelect(BaseModel): ...


class Number(BaseModel): ...


class People(BaseModel): ...


class PhoneNumber(BaseModel): ...


class Relation(BaseModel): ...


class Rollup(BaseModel): ...


class Select(BaseModel): ...


class Status(BaseModel): ...


class Title(BaseModel): ...


class Url(BaseModel): ...
