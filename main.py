import os
import typer
from dotenv import load_dotenv
from rich import print
from notion_toolkit.notion import Notion

load_dotenv()

DATABASE_ID = "54ab647b7e4949d4972d4d5ede8b48ce"


def main():
    writer = Notion(token=os.getenv("NOTION_TOKEN"))
    response = writer.create_page(database_id=DATABASE_ID, title="test_123")
    print(response)


if __name__ == "__main__":
    typer.run(main)
