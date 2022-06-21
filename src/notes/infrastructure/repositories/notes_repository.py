from typing import List

from notes.application.repositories import NotesAbstractRepository
from notes.domain.entities import Note
from notes.domain.value_objects import NoteID


class NotesSqlAlchemyRepository(NotesAbstractRepository):

    def __init__(self, session) -> None:
        self.session = session

    def get(self, note_id: NoteID) -> Note:
        return self.session.query(Note).filter_by(id=note_id).one()

    def save(self, note: Note) -> None:
        self.session.add(note)

    def list(self) -> List[Note]:
        return self.session.query(Note).all()
