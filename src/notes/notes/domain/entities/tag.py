from uuid import UUID

from typing_extensions import TypeAlias

TagID: TypeAlias = UUID
TagName: TypeAlias = str


class Tag:
    """Tag entity class."""

    def __init__(self, id: TagID, name: TagName) -> None:
        self.id = id
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return False
        return other.id == self.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'<Tag id={self.id}, name={self.name}>'

    def __str__(self) -> str:
        return f'Tag {self.id}'
