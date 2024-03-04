"""Block Schema.

Official Notion API
    - https://developers.notion.com/reference/block

"""

from pydantic import BaseModel, Field


class RichText(BaseModel):
    """Rich Text.

    Official Notion API
        - https://developers.notion.com/reference/rich-text

    """
