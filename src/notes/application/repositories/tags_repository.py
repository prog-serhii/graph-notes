import abc

from notes.domain.entities import Tag
from notes.domain.value_objects import TagID


class TagsAbstractRepository(abc.ABC):

    @abc.abstractclassmethod
    def get(self, tag_id: TagID) -> Tag:
        raise NotImplementedError

    @abc.abstractclassmethod
    def save(self, tag: Tag) -> None:
        raise NotImplementedError
