from typing import List
from typing_extensions import TypeAlias
from uuid import UUID

from notes.domain.entities.note import NoteID
from notes.domain.entities.tag import TagID


UserID: TypeAlias = UUID


class User:
    """User entity class."""

    def __init__(self, id: UserID) -> None:
        self.id = id
        self.notes = List[NoteID]
        self.tags = List[TagID]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return other.id == self.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'<User id={self.id}, notes={self.notes}, tags={self.tags}>'

    def __str__(self) -> str:
        return f'User {self.id}'
