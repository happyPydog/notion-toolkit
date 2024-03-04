"""Parent object schema."""

from pydantic import BaseModel, UUID4


class DatabaseParent(BaseModel):
    """Database parent object."""

    type: str = "database_id"
    database_id: str | UUID4


class PageParent(BaseModel):
    """Page parent object."""

    type: str = "page_id"
    page_id: str | UUID4


class WorkspaceParent(BaseModel):
    """Workspace parent object."""

    type: str = "workspace"
    workspace: bool


class BlockParent(BaseModel):
    """Block parent object."""

    type: str = "block_id"
    block_id: str | UUID4
