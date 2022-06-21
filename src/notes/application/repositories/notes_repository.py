import abc

from notes.domain.entities import Note
from notes.domain.value_objects import NoteID


class NotesAbstractRepository(abc.ABC):

    @abc.abstractclassmethod
    def get(self, note_id: NoteID) -> Note:
        raise NotImplementedError

    @abc.abstractclassmethod
    def save(self, note: Note) -> None:
        raise NotImplementedError
