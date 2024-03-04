import os
from notion_client import Client
from typing_extensions import Unpack

from notion_toolkit.schema.page import ProdCopilotSourceDatabasePageRequestBody


class Notion:

    def __init__(self, token: str | None = None):
        self.token = token or os.environ.get("NOTION_TOKEN")
        self._client = Client(auth=token)

    @property
    def client(self):
        """Notion client."""
        return self._client

    def create_page(
        self,
        database_id: str,
    ) -> NotionPageResponse:

        request_body = self._create_page_request_body()
        page_response = self.client.pages.create(
            parent={"database_id": database_id},
            properties=self._create_properties(**kwargs),
            icon={"type": "emoji", "emoji": "🎥"},
        )

        return page_response

    def _create_page_request_body(
        self,
        title: str,
    ) -> ProdCopilotSourceDatabasePageRequestBody:
        return ProdCopilotSourceDatabasePageRequestBody()

    def _create_properties(
        self,
        title: str,
        text_link: str | None = None,
        bold: bool = False,
        italic: bool = False,
        strikethrough: bool = False,
        underline: bool = False,
        code: bool = False,
        color: str = "default",
        href: str | None = None,
        archived: bool = False,
        source_type: ProdCopilotSourceType = ProdCopilotSourceType.WEBPAGE,
        tags: list[str] | None = None,
        url: str | None = None,
    ) -> dict:
        return {
            "Name": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": title,
                            "link": text_link,
                        },
                        "annotations": {
                            "bold": bold,
                            "italic": italic,
                            "strikethrough": strikethrough,
                            "underline": underline,
                            "code": code,
                            "color": color,
                        },
                        "plain_text": title,
                        "href": href,
                    }
                ],
            },
            "Archived": {"checkbox": archived},
            "Tags": {
                "type": "multi_select",
                "multi_select": [{"name": tag} for tag in tags or {}],
            },
            "Source_Type": {
                "type": "select",
                "select": {"name": source_type},
            },
            "URL": {"url": url},
        }
