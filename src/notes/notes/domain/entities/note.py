from typing import List
from typing_extensions import TypeAlias
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
        self.tags = List[TagID]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Note):
            return False
        return other.id == self.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'<Note id={self.id}, title={self.title}, tags={self.tags}>'

    def __str__(self) -> str:
        return f'Note {self.id}'
