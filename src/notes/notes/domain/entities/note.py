from typing import List
from typing_extensions import TypeAlias
from unittest.mock import NonCallableMagicMock
from uuid import UUID

from notes.domain.entities.tag import TagID


NoteID: TypeAlias = UUID
NoteTitle: TypeAlias = str
NoteContent: TypeAlias = str


class Note:
    """Note entity class."""

    def __init__(
        self, id: NoteID, title: NoteTitle, content: NoteContent
    ) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.tags: List[TagID] = []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Note):
            return False
        return other.id == self.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return (
            f'<Note id={self.id}, title={self.title}, '
            f'content={self.content}, tags={self.tags}>'
        )

    def __str__(self) -> str:
        return f'Note {self.id}'

    def can_add_tag(self, tag_id: TagID) -> bool:
        return tag_id not in self.tags

    def add_tag(self, tag_id: TagID) -> None:
        if self.can_add_tag(tag_id):
            self.tags.append(tag_id)

    def can_remove_tag(self, tag_id: TagID) -> bool:
        return tag_id in self.tags

    def remove_tag(self, tag_id: TagID) -> None:
        if self.can_remove_tag(tag_id):
            self.tags.remove(tag_id)
