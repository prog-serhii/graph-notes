from typing import List

from notes.application.repositories import TagsAbstractRepository
from notes.domain.entities import Tag
from notes.domain.value_objects import TagID


class TagsSqlAlchemyRepository(TagsAbstractRepository):

    def __init__(self, session) -> None:
        self.session = session

    def get(self, tag_id: TagID) -> Tag:
        return self.session.query(Tag).filter_by(id=tag_id).one()

    def save(self, tag: Tag) -> None:
        self.session.add(tag)

    def list(self) -> List[Tag]:
        return self.session.query(Tag).all()
